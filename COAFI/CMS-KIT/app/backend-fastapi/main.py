#!/usr/bin/env python3
"""
Main entry point for COAFI FastAPI backend.
Initializes routers, middleware, and memory services.
"""

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import zipfile, os, tempfile, subprocess, shutil
import mimetypes

# Import your custom routers
from routers.services import semantic_bridge  # <-- asegúrate que semantic_bridge.py tiene router = APIRouter()
from routers import review  # Import the new review router
from core.memory.memory_service import memory_service  # Import the memory service
from api_orchestration.src.OrchestrationBuilder import OrchestrationBuilder  # Import the OrchestrationBuilder
from routers.services import digital_twin_router  # Import the digital twin router

app = FastAPI(
    title="COAFI Quantum Memory API",
    description="API para operaciones de memoria semántica, integración con vectores y dashboard",
    version="0.1.0"
)

# Enable CORS for local development / UI frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LANG_COMMANDS = {
    '.py': ['python'],
    '.js': ['node'],
    '.sh': ['bash'],
}

TEST_FILE_PATTERNS = ['test_', '.spec.']

@app.post("/run-zip/")
async def run_zip(file: UploadFile):
    if file.content_type != "application/zip":
        raise HTTPException(status_code=400, detail="File must be a ZIP archive.")

    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, file.filename)
        
        with open(zip_path, "wb") as f:
            f.write(await file.read())

        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(tmpdir)
        except zipfile.BadZipFile:
            raise HTTPException(status_code=400, detail="Invalid ZIP file.")

        results = execute_files(tmpdir)

        return results

def execute_files(directory):
    results = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_ext = os.path.splitext(file)[1]
            cmd = LANG_COMMANDS.get(file_ext)
            
            if cmd:
                filepath = os.path.join(root, file)
                exec_cmd = cmd + [filepath]

                # Check if it's a test file
                is_test = any(pattern in file for pattern in TEST_FILE_PATTERNS)

                try:
                    completed_process = subprocess.run(
                        exec_cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=10,
                        text=True
                    )

                    results[file] = {
                        "test_file": is_test,
                        "stdout": completed_process.stdout.strip(),
                        "stderr": completed_process.stderr.strip(),
                        "returncode": completed_process.returncode,
                    }

                except subprocess.TimeoutExpired:
                    results[file] = {
                        "test_file": is_test,
                        "error": "Execution timeout",
                        "returncode": -1
                    }
                except Exception as e:
                    results[file] = {
                        "test_file": is_test,
                        "error": str(e),
                        "returncode": -1
                    }

    return results

@app.get("/document-interdependencies")
async def document_interdependencies():
    return await memory_service.getDocumentInterdependencies()

@app.get("/document-status")
async def document_status():
    return await memory_service.getDocumentStatus()

@app.post("/update-related-documents")
async def update_related_documents(document_id: str):
    return await memory_service.updateRelatedDocuments(document_id)

@app.post("/integrate-version-control")
async def integrate_version_control():
    return await memory_service.integrateVersionControl()

@app.post("/generate-document")
async def generate_document(request: dict):
    orchestrator = OrchestrationBuilder("DocumentGenerationOrchestrator")
    return await orchestrator.generateTechnicalReferenceDocument(request)

@app.post("/seed-module")
async def seed_module(module_name: str):
    orchestrator = OrchestrationBuilder("ModuleSeedingOrchestrator")
    return await orchestrator.seedModule(module_name)

@app.post("/render-federation")
async def render_federation(federation_description: str):
    orchestrator = OrchestrationBuilder("FederationRenderingOrchestrator")
    return await orchestrator.renderFederation(federation_description)

@app.post("/amplify-ampel")
async def amplify_ampel(article_description: str):
    orchestrator = OrchestrationBuilder("AmpelAmplificationOrchestrator")
    return await orchestrator.amplifyAmpel(article_description)

@app.post("/deploy-agad")
async def deploy_agad(axis_description: str):
    orchestrator = OrchestrationBuilder("AgadDeploymentOrchestrator")
    return await orchestrator.deployAgad(axis_description)

@app.post("/export-memseed")
async def export_memseed(memseed_name: str):
    orchestrator = OrchestrationBuilder("MemseedExportOrchestrator")
    return await orchestrator.exportMemseed(memseed_name)

@app.post("/init-temporal")
async def init_temporal(session_description: str):
    orchestrator = OrchestrationBuilder("TemporalSessionOrchestrator")
    return await orchestrator.initTemporal(session_description)

@app.post("/execute-phi-mode")
async def execute_phi_mode(request: dict):
    orchestrator = OrchestrationBuilder("PhiModeExecutionOrchestrator")
    return await orchestrator.executePhiMode(request)

@app.post("/execute-ethical-promptimization")
async def execute_ethical_promptimization(request: dict):
    orchestrator = OrchestrationBuilder("EthicalPromptimizationOrchestrator")
    return await orchestrator.executeEthicalPromptimization(request)

# Mount routers
app.include_router(semantic_bridge.router, prefix="/semantic-query", tags=["Semantic Query"])
app.include_router(review.router, prefix="/review", tags=["Year-End Review"])  # Include the new review router
app.include_router(digital_twin_router.router, prefix="/digital-twin", tags=["Digital Twin"])  # Include the digital twin router

# Health check route
@app.get("/")
def read_root():
    return {"status": "COAFI API running", "docs": "/docs", "semantic": "/semantic-query"}

# Entry point
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

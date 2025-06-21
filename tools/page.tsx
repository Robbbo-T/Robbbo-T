import { IntegratedQuantumPredictor } from "@/components/quantum-maintenance/integrated-quantum-predictor"
import { IntegrationDiagram } from "@/components/quantum-maintenance/integration-diagram"
import { Separator } from "@/components/ui/separator"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Info } from "lucide-react"

export default function IntegratedQuantumMaintenancePage() {
  return (
    <div className="container mx-auto py-8">
      <div className="flex flex-col items-center justify-center space-y-4 text-center">
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">
          Integrated Quantum-Enhanced Predictive Maintenance
        </h1>
        <p className="max-w-[700px] text-gray-500 md:text-xl">
          Advanced quantum-enhanced algorithmic prediction with ZIP code and image analysis integration
        </p>
      </div>

      <Alert className="my-8">
        <Info className="h-4 w-4" />
        <AlertTitle>Integration Information</AlertTitle>
        <AlertDescription>
          This advanced system integrates quantum predictive maintenance with code analysis from ZIP files and component
          recognition from images. The multi-modal approach significantly improves prediction accuracy and maintenance
          optimization.
        </AlertDescription>
      </Alert>

      <Separator className="my-8" />

      <div className="mb-8">
        <IntegrationDiagram />
      </div>

      <IntegratedQuantumPredictor modelId="hydraulic-system-main" initialCycles={1000} />
    </div>
  )
}

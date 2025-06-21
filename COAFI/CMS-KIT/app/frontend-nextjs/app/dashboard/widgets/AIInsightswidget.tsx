"use client";
import React, { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";

const AIInsightsWidget = () => {
  const [documentInterdependencies, setDocumentInterdependencies] = useState(null);
  const [documentStatus, setDocumentStatus] = useState(null);
  const [updateRelatedDocuments, setUpdateRelatedDocuments] = useState(null);
  const [integrateVersionControl, setIntegrateVersionControl] = useState(null);
  const [generatedDocument, setGeneratedDocument] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/document-interdependencies")
      .then((res) => res.json())
      .then((data) => setDocumentInterdependencies(data))
      .catch(() => setDocumentInterdependencies(null));

    fetch("http://localhost:8000/document-status")
      .then((res) => res.json())
      .then((data) => setDocumentStatus(data))
      .catch(() => setDocumentStatus(null));

    fetch("http://localhost:8000/update-related-documents")
      .then((res) => res.json())
      .then((data) => setUpdateRelatedDocuments(data))
      .catch(() => setUpdateRelatedDocuments(null));

    fetch("http://localhost:8000/integrate-version-control")
      .then((res) => res.json())
      .then((data) => setIntegrateVersionControl(data))
      .catch(() => setIntegrateVersionControl(null));
  }, []);

  const handleGenerateDocument = () => {
    fetch("http://localhost:8000/generate-document", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: "Technical Reference Document",
        content: "This is the content of the technical reference document.",
        metadata: {
          author: "John Doe",
          date: "2023-01-01",
          version: "1.0",
        },
      }),
    })
      .then((res) => res.json())
      .then((data) => setGeneratedDocument(data))
      .catch(() => setGeneratedDocument(null));
  };

  return (
    <motion.div
      className="grid gap-4"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-xl font-semibold">AI Insights</h2>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Document Interdependencies</h3>
          <p className="text-sm text-gray-500">{documentInterdependencies ? JSON.stringify(documentInterdependencies) : "Loading..."}</p>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Document Status</h3>
          <p className="text-sm text-gray-500">{documentStatus ? JSON.stringify(documentStatus) : "Loading..."}</p>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Update Related Documents</h3>
          <p className="text-sm text-gray-500">{updateRelatedDocuments ? JSON.stringify(updateRelatedDocuments) : "Loading..."}</p>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Integrate Version Control</h3>
          <p className="text-sm text-gray-500">{integrateVersionControl ? JSON.stringify(integrateVersionControl) : "Loading..."}</p>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Generate Technical Reference Document</h3>
          <Button onClick={handleGenerateDocument}>Generate Document</Button>
          <p className="text-sm text-gray-500 mt-2">{generatedDocument ? JSON.stringify(generatedDocument) : "No document generated yet."}</p>
        </CardContent>
      </Card>
    </motion.div>
  );
};

export default AIInsightsWidget;

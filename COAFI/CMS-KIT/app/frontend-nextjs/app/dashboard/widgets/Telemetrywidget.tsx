"use client";
import React, { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

const TelemetryWidget = () => {
  const [documentInterdependencies, setDocumentInterdependencies] = useState(null);
  const [documentStatus, setDocumentStatus] = useState(null);
  const [updateRelatedDocuments, setUpdateRelatedDocuments] = useState(null);
  const [integrateVersionControl, setIntegrateVersionControl] = useState(null);

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

  return (
    <motion.div
      className="grid gap-4"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-xl font-semibold">Telemetry</h2>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <p className="text-sm text-gray-500">Live metrics syncing...</p>
        </CardContent>
      </Card>
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
    </motion.div>
  );
};

export default TelemetryWidget;

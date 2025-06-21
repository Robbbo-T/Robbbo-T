import React, { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";
import { User } from "@/types/user";
import { motion } from "framer-motion";

const UsersWidget = () => {
  const [users, setUsers] = useState<User[] | null>(null);
  const [loading, setLoading] = useState(true);
  const [documentInterdependencies, setDocumentInterdependencies] = useState(null);
  const [documentStatus, setDocumentStatus] = useState(null);
  const [updateRelatedDocuments, setUpdateRelatedDocuments] = useState(null);
  const [integrateVersionControl, setIntegrateVersionControl] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/users")
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));

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
      <h2 className="text-xl font-semibold">Users</h2>
      <div className="grid gap-2">
        {loading && <Skeleton className="h-24 w-full rounded-xl" />}
        {!loading && users && users.length > 0 ? (
          users.map((user) => (
            <Card key={user.id} className="shadow-sm">
              <CardContent className="p-4">
                <p className="font-medium">{user.name}</p>
                <p className="text-sm text-gray-500">{user.email}</p>
              </CardContent>
            </Card>
          ))
        ) : (
          !loading && <p className="text-sm text-gray-400">No users found.</p>
        )}
      </div>

      <h2 className="text-xl font-semibold">Document Interdependencies</h2>
      <div className="grid gap-2">
        {documentInterdependencies ? (
          <Card className="shadow-sm">
            <CardContent className="p-4">
              <p className="text-sm text-gray-500">{JSON.stringify(documentInterdependencies)}</p>
            </CardContent>
          </Card>
        ) : (
          <p className="text-sm text-gray-400">No interdependencies found.</p>
        )}
      </div>

      <h2 className="text-xl font-semibold">Document Status</h2>
      <div className="grid gap-2">
        {documentStatus ? (
          <Card className="shadow-sm">
            <CardContent className="p-4">
              <p className="text-sm text-gray-500">{JSON.stringify(documentStatus)}</p>
            </CardContent>
          </Card>
        ) : (
          <p className="text-sm text-gray-400">No status found.</p>
        )}
      </div>

      <h2 className="text-xl font-semibold">Update Related Documents</h2>
      <div className="grid gap-2">
        {updateRelatedDocuments ? (
          <Card className="shadow-sm">
            <CardContent className="p-4">
              <p className="text-sm text-gray-500">{JSON.stringify(updateRelatedDocuments)}</p>
            </CardContent>
          </Card>
        ) : (
          <p className="text-sm text-gray-400">No updates found.</p>
        )}
      </div>

      <h2 className="text-xl font-semibold">Integrate Version Control</h2>
      <div className="grid gap-2">
        {integrateVersionControl ? (
          <Card className="shadow-sm">
            <CardContent className="p-4">
              <p className="text-sm text-gray-500">{JSON.stringify(integrateVersionControl)}</p>
            </CardContent>
          </Card>
        ) : (
          <p className="text-sm text-gray-400">No version control data found.</p>
        )}
      </div>
    </motion.div>
  );
};

export default UsersWidget;

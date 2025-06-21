'use client'

import { useEffect } from 'react'
import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { useDashboardStore } from '@/lib/stores/dashboard'
import { LoaderCircle } from 'lucide-react'

export default function DashboardPage() {
  const { nodes, fetchNodes, loading, documentInterdependencies, documentStatus, updateRelatedDocuments, integrateVersionControl } = useDashboardStore()

  useEffect(() => {
    fetchNodes()
  }, [fetchNodes])

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold tracking-tight">Panel de Control COAFI</h1>
      <p className="text-muted-foreground">Gestión de nodos federados, agentes AI y actividad reciente.</p>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {loading ? (
          <Card className="flex items-center justify-center h-32">
            <LoaderCircle className="animate-spin h-6 w-6 text-gray-500" />
          </Card>
        ) : (
          nodes.map((node, i) => (
            <Card key={i}>
              <CardContent className="p-4">
                <h2 className="font-semibold text-lg">{node.name}</h2>
                <p className="text-sm text-muted-foreground">Estado: {node.status}</p>
                <Button variant="outline" className="mt-2">Ver detalles</Button>
              </CardContent>
            </Card>
          ))
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
        <Card>
          <CardContent className="p-4">
            <h2 className="font-semibold text-lg">Document Interdependencies</h2>
            <p className="text-sm text-muted-foreground">{documentInterdependencies}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <h2 className="font-semibold text-lg">Document Status</h2>
            <p className="text-sm text-muted-foreground">{documentStatus}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <h2 className="font-semibold text-lg">Update Related Documents</h2>
            <p className="text-sm text-muted-foreground">{updateRelatedDocuments}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <h2 className="font-semibold text-lg">Integrate Version Control</h2>
            <p className="text-sm text-muted-foreground">{integrateVersionControl}</p>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

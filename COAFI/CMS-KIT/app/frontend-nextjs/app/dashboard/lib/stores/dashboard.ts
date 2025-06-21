import { create } from 'zustand'
import axios from 'axios'

type NodeInfo = {
  id: string
  name: string
  status: string
  lastPing: string
}

type UserMetric = {
  total: number
  active: number
  suspended: number
}

type AgentActivity = {
  id: string
  name: string
  role: string
  lastAction: string
}

type DashboardState = {
  loading: boolean
  nodes: NodeInfo[]
  users: UserMetric | null
  agents: AgentActivity[]
  documentInterdependencies: string | null
  documentStatus: string | null
  updateRelatedDocuments: string | null
  integrateVersionControl: string | null
  fetchDashboard: () => void
  fetchDocumentInterdependencies: () => void
  fetchDocumentStatus: () => void
  fetchUpdateRelatedDocuments: () => void
  fetchIntegrateVersionControl: () => void
}

export const useDashboardStore = create<DashboardState>((set) => ({
  loading: true,
  nodes: [],
  users: null,
  agents: [],
  documentInterdependencies: null,
  documentStatus: null,
  updateRelatedDocuments: null,
  integrateVersionControl: null,
  fetchDashboard: async () => {
    set({ loading: true })
    try {
      const [nodesRes, usersRes, agentsRes] = await Promise.all([
        axios.get('/api/nodes'),
        axios.get('/api/users/metrics'),
        axios.get('/api/agents/activity')
      ])

      set({
        nodes: nodesRes.data,
        users: usersRes.data,
        agents: agentsRes.data,
        loading: false
      })
    } catch (err) {
      console.error('Dashboard fetch error:', err)
      set({ loading: false })
    }
  },
  fetchDocumentInterdependencies: async () => {
    try {
      const response = await axios.get('/api/document-interdependencies')
      set({ documentInterdependencies: response.data })
    } catch (err) {
      console.error('Error fetching document interdependencies:', err)
    }
  },
  fetchDocumentStatus: async () => {
    try {
      const response = await axios.get('/api/document-status')
      set({ documentStatus: response.data })
    } catch (err) {
      console.error('Error fetching document status:', err)
    }
  },
  fetchUpdateRelatedDocuments: async () => {
    try {
      const response = await axios.get('/api/update-related-documents')
      set({ updateRelatedDocuments: response.data })
    } catch (err) {
      console.error('Error fetching update related documents:', err)
    }
  },
  fetchIntegrateVersionControl: async () => {
    try {
      const response = await axios.get('/api/integrate-version-control')
      set({ integrateVersionControl: response.data })
    } catch (err) {
      console.error('Error fetching integrate version control:', err)
    }
  }
}))

Here is the `generateMarkdown.ts` file content you provided:

```ts
export function generateMarkdown(logs: { code: string; description: string; status: string }[]) {
  const now = new Date().toLocaleString('es-ES');

  const table = logs
    .map(log => `| ${log.code} | ${log.description} | ${log.status} |`)
    .join('\n');

  const status = logs.some(l => l.status.includes('❌')) ? '⚠️ Requiere atención' : '🟢 Operativo';

  return `
# ✅ Robbbo-T Operational Success Log

**Última actualización**: ${now}

## Escenarios registrados

| Código | Evento | Resultado |
|--------|--------|-----------|
${table}

---

**Estado del Sistema**: ${status}

Versión: \`ROBBBO-T-GAIA-ICSDB-001\`
`;
}
```

You can place this content in the file located at `/components/robbbot/utils/generateMarkdown.ts` in your repository. If you need further assistance with integrating this or any other part of your project, please let me know!

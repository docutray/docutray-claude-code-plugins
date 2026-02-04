# DevFlow Flow Skills for Kimi CLI

Flow Skills de DevFlow adaptadas para Kimi CLI, proporcionando workflows de desarrollo agile automatizados.

## Flow Skills Disponibles

| Flow Skill | Descripción | Comando |
|------------|-------------|---------|
| `devflow-feat` | Crear especificaciones de features y GitHub issues | `/flow:devflow-feat` |
| `devflow-dev` | Implementar features desde GitHub issues | `/flow:devflow-dev` |
| `devflow-check` | Ejecutar validaciones en paralelo | `/flow:devflow-check` |
| `devflow-review-pr` | Revisar Pull Requests | `/flow:devflow-review-pr` |
| `devflow-research` | Investigar topics antes de planificar | `/flow:devflow-research` |
| `devflow-epic` | Crear epics con múltiples fases | `/flow:devflow-epic` |

## Instalación

### Método 1: Copiar (Recomendado para usuarios)

```bash
# Desde el repositorio
cd docutray-claude-code-plugins
./install-kimi-flows.sh
```

### Método 2: Symlink (Para desarrollo)

```bash
# Los cambios en el repo se reflejan automáticamente
./install-kimi-flows.sh --symlink
```

### Método 3: Manual

```bash
# Copiar skills a directorio de Kimi
mkdir -p ~/.config/agents/skills/
cp -r .kimi/skills/devflow-* ~/.config/agents/skills/
```

## Flujo de Trabajo

### Feature Estándar

```
/flow:devflow-feat     → Crear especificación e issue
/flow:devflow-dev     → Implementar feature
/flow:devflow-check   → Validar código
/flow:devflow-review-pr → Revisar PR
```

### Epic (Iniciativa Grande)

```
/flow:devflow-research → Investigar tecnología
/flow:devflow-epic     → Crear epic con fases
/flow:devflow-feat     → Crear specs para componentes
/flow:devflow-dev      → Implementar cada componente
/flow:devflow-review-pr → Revisar cada PR
```

## Estructura

```
.kimi/
└── skills/
    ├── devflow-feat/SKILL.md        # Crear features
    ├── devflow-dev/SKILL.md         # Implementar
    ├── devflow-check/SKILL.md       # Validar
    ├── devflow-review-pr/SKILL.md   # Revisar PRs
    ├── devflow-research/SKILL.md    # Investigar
    └── devflow-epic/SKILL.md        # Planificar epics
```

## Diferencias con Claude Code Plugins

| Aspecto | Claude Code | Kimi CLI |
|---------|-------------|----------|
| Formato | Slash commands | Flow Skills |
| Activación | `/devflow:feat` | `/flow:devflow-feat` |
| Ejecución | Single-shot | Multi-step automatizado |
| Decisiones | Usuario decide | Flow diagram con choices |

## Compatibilidad

- **Kimi CLI**: ✅ Totalmente compatible
- **Claude Code**: ❌ No afecta (directorio separado)
- **Otras herramientas**: Compatible con cualquier herramienta que use Agent Skills

## Documentación

Cada SKILL.md contiene:
- Diagrama de flujo Mermaid
- Descripción de cada nodo
- Parámetros soportados
- Ejemplos de uso

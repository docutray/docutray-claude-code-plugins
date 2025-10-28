# Check Command Configuration - TypeScript/Node.js

This file configures the `/check` command validations for TypeScript/Node.js projects.

## Validation Configuration

```json
{
  "validations": {
    "tests": {
      "command": "npm run test",
      "description": "Jest/Vitest test suite",
      "enabled": true
    },
    "lint": {
      "command": "npm run lint",
      "description": "ESLint code quality validation",
      "enabled": true
    },
    "typecheck": {
      "command": "npx tsc --noEmit",
      "description": "TypeScript strict type validation (without --skipLibCheck)",
      "enabled": true
    },
    "build": {
      "command": "npm run build",
      "description": "Project build compilation",
      "enabled": true,
      "skip_on_fast": true
    }
  }
}
```

## Customization Guide

### Test Command
- Default: `npm run test`
- For specific packages in monorepo: `npm run test --filter=<package>`
- **For Vitest**: `npx vitest run`
- **Vitest with coverage**: `npx vitest run --coverage`
- **Vitest UI mode**: `npx vitest --ui` (interactive browser interface)
- For specific test file: `npm run test -- <path>`
- **Coverage threshold validation**: Add to vitest.config.ts:
  ```typescript
  test: {
    coverage: {
      thresholds: {
        statements: 80,
        branches: 75,
        functions: 80,
        lines: 80,
      },
    },
  }
  ```

### Lint Command
- Default: `npm run lint`
- For fix mode: `npm run lint -- --fix`
- For specific paths: `npm run lint -- src/`

### Type Check Command
- **Important**: Always run without `--skipLibCheck` for strict validation
- Default: `npx tsc --noEmit`
- For monorepo: `npx turbo run type-check` or `npx tsc --build`
- The `--skipLibCheck` flag in tsconfig.json is for dev speed only

### Build Command
- Default: `npm run build`
- For Next.js: `npm run build` (includes type checking)
- For monorepo: `npx turbo run build`
- For specific package: `npm run build --filter=<package>`

## Vitest-Specific Configuration

### Coverage Providers

Vitest supports two coverage providers:

**@vitest/coverage-v8** (Recommended - faster):
```bash
npm install -D @vitest/coverage-v8
```

**@vitest/coverage-istanbul** (More accurate):
```bash
npm install -D @vitest/coverage-istanbul
```

Configure in vitest.config.ts:
```typescript
export default {
  test: {
    coverage: {
      provider: 'v8', // or 'istanbul'
      reporter: ['text', 'json', 'html', 'lcov'],
      exclude: [
        'node_modules/',
        'test/',
        '**/*.spec.ts',
        '**/*.test.ts',
      ],
    },
  },
};
```

### Test Command with Coverage in CI

For CI/CD pipelines:
```json
{
  "validations": {
    "tests": {
      "command": "npx vitest run --coverage --reporter=verbose",
      "description": "Vitest with coverage and verbose output",
      "enabled": true
    }
  }
}
```

## Additional Validations

You can add custom validations:

```json
{
  "validations": {
    "...": "...",
    "coverage": {
      "command": "npx vitest run --coverage",
      "description": "Tests with coverage report",
      "enabled": false
    },
    "format": {
      "command": "npm run format:check",
      "description": "Prettier format validation",
      "enabled": false
    },
    "audit": {
      "command": "npm audit --audit-level=high",
      "description": "Security audit",
      "enabled": false
    }
  }
}
```

## Monorepo Configuration

For Turborepo/pnpm workspaces:

```json
{
  "validations": {
    "tests": {
      "command": "npx turbo run test",
      "description": "All workspace tests",
      "enabled": true
    },
    "lint": {
      "command": "npx turbo run lint",
      "description": "All workspace linting",
      "enabled": true
    },
    "typecheck": {
      "command": "npx turbo run type-check",
      "description": "All workspace type checking",
      "enabled": true
    },
    "build": {
      "command": "npx turbo run build",
      "description": "All workspace builds",
      "enabled": true,
      "skip_on_fast": true
    }
  }
}
```

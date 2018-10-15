```json
{
    "compilerOptions": {
        "importHelpers": true,
        "target": "es2015",
        "lib": ["es6", "dom"],
        "module": "commonjs",
        "noResolve": false,
        "allowJs": true,
        "strict": true,
        "jsx": "react",
        "noEmit": true,
        "noImplicitReturns": true,
        "noImplicitThis": true,
        "noImplicitAny": false,
        "moduleResolution": "node",
        "strictNullChecks": true,
        "typeRoots": [
            "node_modules/@types",
            "@types"
        ]
    },
    "exclude": [
        "node_modules",
        "dest",
        "android",
        "ios",
        "acceptance-tests",
        ".jest",
        "src/setupTests.ts",
        "./node_modules/**/*"
    ],
    "types": [
        "typePatches"
    ]
}
```
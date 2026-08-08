# Instalação — Jornada Invisível Mapper

Guia rápido para instalar esta skill em diferentes agentes de IA.

## Estrutura do pacote

```
jornada-invisivel-mapper/
├── SKILL.md                      # Instruções da skill
├── README.md                     # Documentação geral
├── INSTALL.md                    # Este arquivo
└── scripts/
    └── validar_relatorio.py      # Validador determinístico
```

## Kimi CLI

Copie a pasta para o diretório de skills do Kimi CLI:

```bash
# Linux / macOS
cp -r jornada-invisivel-mapper ~/.kimi/skills/

# Windows (PowerShell)
Copy-Item -Recurse -Path jornada-invisivel-mapper -Destination $env:USERPROFILE\.kimi\skills\
```

Reinicie o Kimi CLI. A skill será carregada automaticamente a partir do frontmatter do `SKILL.md`.

## Claude Code

Copie a pasta para o diretório de skills do Claude Code:

```bash
# Linux / macOS
cp -r jornada-invisivel-mapper ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse -Path jornada-invisivel-mapper -Destination $env:USERPROFILE\.claude\skills\
```

Reinicie o Claude Code. A skill será descoberta automaticamente.

## Hermes Agent

Copie a pasta para o diretório de skills do Hermes:

```bash
# Linux / macOS
cp -r jornada-invisivel-mapper ~/.hermes/skills/

# Windows (PowerShell)
Copy-Item -Recurse -Path jornada-invisivel-mapper -Destination $env:USERPROFILE\.hermes\skills\
```

Ou adicione como diretório externo em `~/.hermes/config.yaml`:

```yaml
skills:
  external_dirs:
    - ~/.agents/skills
```

Reinicie o Hermes. A skill estará disponível como `/jornada-invisivel-mapper`.

## Uso do validador

Antes de entregar qualquer relatório gerado pela skill, execute:

```bash
# Linux / macOS / Hermes
python3 scripts/validar_relatorio.py <relatorio.md>

# Windows / Kimi CLI / Claude Code
python scripts\validar_relatorio.py <relatorio.md>
```

Qualquer resultado **FAIL** bloqueia a entrega. Corrija o relatório e rode novamente até obter **PASS**.

## Instalação via Git

Se preferir clonar diretamente:

```bash
git clone https://github.com/alanvitorino/skill_-journey_invisible.git
```

Depois copie a pasta clonada para o diretório de skills do agente desejado.

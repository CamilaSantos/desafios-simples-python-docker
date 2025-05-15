#!/bin/bash

ROOT_DIR="APRENDENDO/Desafios_Python"
LAUNCH_FILE=".vscode/launch.json"

# Função para gerar uma configuração de depuração
generate_config() {
  local folder="$1"
  local script_name=$(basename "$folder" ".py")
  local config_name="Python Debugger: Remote Attach ($(basename "$folder"))"
  local local_root="\${workspaceFolder}/Desafios_Python/$folder"

  cat <<EOF
            {
                "name": "${config_name}",
                "type": "debugpy",
                "request": "attach",
                "connect": {
                    "host": "localhost",
                    "port": 5678
                },
                "pathMappings": [
                    {
                        "localRoot": "${local_root}",
                        "remoteRoot": "/app"
                    }
                ]
            }
EOF
}

# Limpar o arquivo launch.json
echo '{
    "version": "0.2.0",
    "configurations": [' > "$LAUNCH_FILE"

# Flag para controlar a vírgula entre as configurações
first=true

# Encontrar pastas dentro do diretório raiz
find "$ROOT_DIR" -maxdepth 1 -mindepth 1 -type d | while IFS= read -r folder; do
  # Procurar por arquivos .py dentro de cada pasta
  find "$folder" -maxdepth 1 -name "*.py" -print0 | while IFS= read -r -d $'\0' script_path; do
    local script_folder=$(dirname "$script_path")
    local relative_folder=$(echo "$script_folder" | sed "s|^$ROOT_DIR/||")

    if "$first"; then
      first=false
    else
      echo "," >> "$LAUNCH_FILE"
    fi
    generate_config "$relative_folder"
    echo >> "$LAUNCH_FILE"
  done
done

# Fechar o array de configurações
echo '    ]
}' >> "$LAUNCH_FILE"

echo "Arquivo $LAUNCH_FILE gerado/atualizado."
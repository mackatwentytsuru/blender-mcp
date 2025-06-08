# 🐳 Docker環境でのBlenderMCP マルチクライアント接続ガイド

このガイドでは、DockerでMCPサーバーを起動し、Claude Desktop、Claude Code、Cursorの3つのクライアントから同時に接続する方法を説明します。

## 🌟 主な特徴

- 🤖 3つのAIクライアント（Claude Desktop、Claude Code、Cursor）から同時接続
- 🔄 Blender起動時の自動接続機能
- 🛠️ 簡単なセットアップスクリプト
- 🐳 Dockerによる一貫した実行環境

## 🏗️ アーキテクチャ構成

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Claude    │     │   Claude    │     │   Cursor    │
│   Desktop   │     │    Code     │     │             │
│  (Windows)  │     │   (WSL2)    │     │  (Windows)  │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                     │
       └───────────────────┼─────────────────────┘
                           │
                    ┌──────▼──────┐
                    │   Docker    │
                    │ MCP Server  │
                    │   (WSL2)    │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Blender   │
                    │  (Windows)  │
                    │ Port: 9876  │
                    └─────────────┘
```

## 1. 前提条件

- Windows上にBlenderがインストールされている
- WSL2上にDockerがインストールされている
- Claude Desktop、Claude Code、Cursorがインストールされている

## 2. セットアップ手順

### 2.1 WSL2でのDocker起動

1. WSL2ターミナルを開き、プロジェクトディレクトリに移動：
```bash
cd /mnt/h/Yuki\ Tsuruoka\ Dropbox/鶴岡悠生/AI\ Clasude\ code/Blender\ MCP/blender-mcp
```

2. 環境変数ファイルを作成（オプション）：
```bash
cp .env.example .env
# 必要に応じてAPIキーを設定
```

3. Dockerコンテナを起動：
```bash
docker-compose up -d
```

4. コンテナが正常に起動したか確認：
```bash
docker ps
docker logs blender-mcp-server
```

### 2.2 Blenderの設定

1. Windows上でBlenderを起動
2. BlenderMCPアドオンをインストール：
   - Edit → Preferences → Add-ons → Install
   - `addon.py`ファイルを選択
   - 「BlenderMCP」アドオンを有効化 ✅

3. **🎉 自動起動機能**: アドオンを有効化すると、Blender起動時に自動的にMCPサーバーが開始されます！
   - デフォルトポート: 9876
   - リッスンアドレス: 0.0.0.0（すべてのインターフェース）

### 2.3 各クライアントの設定

#### Claude Desktop (Windows)

1. Claude Desktopの設定ファイルを開く：
   - 場所: `%APPDATA%\Claude\claude_desktop_config.json`

2. 以下の設定を追加：
```json
{
  "mcpServers": {
    "blender-mcp": {
      "command": "wsl",
      "args": ["-e", "docker", "exec", "-i", "blender-mcp-server", "blender-mcp"]
    }
  }
}
```

3. Claude Desktopを再起動

#### Claude Code (WSL2)

**⚠️ 重要**: Claude Codeには既知の問題があり、グローバル設定が正しく機能しません（[GitHub Issue #515](https://github.com/anthropics/claude-code/issues/515)）。

**推奨方法 1: ヘルパースクリプトを使用**
```bash
# BlenderMCPを現在のプロジェクトに追加
~/mcp設定ツール/add-blender-mcp.sh

# すべてのMCPツールを追加（Docker MCP、GitHub MCPなども含む）
~/mcp設定ツール/add-all-mcp.sh
```

**推奨方法 2: 手動でプロジェクトごとに追加**
```bash
claude mcp add blender-mcp docker exec -i blender-mcp-server blender-mcp
```

**参考: グローバル設定（将来のバグ修正後）**
```bash
# ~/.claude/settings.json に追加
{
  "mcpServers": {
    "blender-mcp": {
      "type": "stdio",
      "command": "docker",
      "args": ["exec", "-i", "blender-mcp-server", "blender-mcp"]
    }
  }
}
```

#### Cursor (Windows)

1. Cursorの設定から「MCP」セクションを開く
2. 以下の設定を追加：
```json
{
  "blender-mcp": {
    "command": "wsl",
    "args": ["-e", "docker", "exec", "-i", "blender-mcp-server", "blender-mcp"]
  }
}
```

## 3. 接続テスト

各クライアントで以下のコマンドを実行して接続を確認：

```
Test the Blender connection
```

正常に接続されている場合、Blenderのバージョン情報が表示されます。

## 4. トラブルシューティング

### 🔧 接続の問題

#### WSL2からWindowsホストへの接続

1. **WindowsのIPアドレスを確認**:
   ```bash
   # WSL2から実行
   ip route | grep default | awk '{print $3}'
   # 通常は 172.31.32.1 のような形式
   ```

2. **docker-compose.ymlの環境変数を更新**:
   ```yaml
   environment:
     - BLENDER_HOST=172.31.32.1  # 上記で確認したIPアドレス
     - BLENDER_PORT=9876
   ```

3. **Windowsファイアウォールの設定**:
   - WSL2からのポート9876への接続を許可
   - Blenderを「プライベートネットワーク」として許可

#### "Connection refused"エラーの場合

1. **Blenderアドオンが0.0.0.0でリッスンしているか確認**:
   - BlenderのSystem Consoleでログを確認
   - "MCP server started on 0.0.0.0:9876"と表示されているか

2. **Dockerコンテナの環境変数を確認**:
   ```bash
   docker exec blender-mcp-server env | grep BLENDER
   ```

### ポート転送の設定

必要に応じてWindowsとWSL2間のポート転送を設定：

```powershell
# PowerShell (管理者権限)で実行
netsh interface portproxy add v4tov4 listenport=8080 listenaddress=0.0.0.0 connectport=8080 connectaddress=127.0.0.1
```

### Docker内からの接続確認

```bash
# コンテナ内でテスト
docker exec -it blender-mcp-server bash
nc -zv host.docker.internal 9876
```

## 5. 停止と再起動

### サービスの停止
```bash
docker-compose down
```

### サービスの再起動
```bash
docker-compose restart
```

### ログの確認
```bash
docker-compose logs -f
```

## 📝 注意事項

- ✅ 3つのクライアントから同時に接続可能ですが、Blenderへの操作は順次実行されます
- ⏳ 大きなファイルの転送やレンダリングなど、時間のかかる操作は他のクライアントをブロックする可能性があります
- 🔐 APIキーを使用する場合は、`.env`ファイルで管理することを推奨します
- 🔄 Blenderを再起動すると、アドオンが自動的にMCPサーバーを開始します
- 💡 WSL2のIPアドレスは再起動時に変更される可能性があるため、接続エラーが発生した場合は再確認してください

## 🚀 クイックスタート

1. **Dockerを起動**: `docker-compose up -d`
2. **Blenderを起動**: アドオンが自動的にサーバーを開始
3. **クライアントから接続**: 各クライアントの設定に従って接続
4. **動作確認**: "Create a red cube"などのコマンドを実行

## 📚 関連ドキュメント

- [README.md](README.md) - プロジェクトの概要
- [CLAUDE.md](CLAUDE.md) - 開発者向けガイド
- [Docker Compose設定](docker-compose.yml) - Docker構成の詳細
# <img src="assets/icon.png" alt="" width="64" height="64" align="absmiddle"> AI家庭教師

**AIに作ってもらったら、次は「AI家庭教師」。**

コード・PR・設計書を教材に、説明、具体例、小さな実践を通して、自分で説明・応用できるところまで学ぶためのSkill／プロンプトです。自分がAIに作ってもらったものだけでなく、他人のPRや既存コードも教材にできます。

## 2つの使い方

| モード | 使う場面 | 呼び出し例 |
|---|---|---|
| セルフ家庭教師 | 実装・技術を理解したい | この変更についてAI家庭教師 |
| レビュー支援 | 同僚との技術会話の観点を整理したい | このPRの観点を5点以内で。AI家庭教師 レビュー支援モード |

セルフ家庭教師は「現在の理解→基礎説明→具体例→ミニ実践→元の教材→自分の言葉で説明」を状況に合わせて進めます。「分かりません」「まず説明して」「別の例で」も歓迎します。

レビュー支援は、教材に即した短い質問を最大5点提示します。先輩自身も「この観点を自分にも教えて」と学べます。通常のコードレビューや人間の判断を代替するものではありません。

## 導入

| 環境 | 配布ファイル | 初回準備・呼び出し |
|---|---|---|
| Codex | [SKILL.md](skills/ai-tutor/SKILL.md) | `.agents/skills/ai-tutor/SKILL.md`として配置。`$ai-tutor`＋対象を指定 |
| Claude Code | [SKILL.md](skills/ai-tutor/SKILL.md) | `.claude/skills/ai-tutor/SKILL.md`として配置。`/ai-tutor`＋対象を指定 |
| CopilotのPrompt file対応環境 | [Prompt file](prompts/copilot/ai-tutor.prompt.md) | `.github/prompts/`へコピー。対応チャットで`/ai-tutor` |
| Web UI | [初期設定プロンプト](prompts/web/ai-tutor.webui.md) | 新しいチャットで全文を一度送信。その後`AI家庭教師` |
| ファイル配置ができない環境 | [最小プロンプト](prompts/ai-tutor-minimal.txt) | 許可された対象と一緒に毎回貼り付け |

Codex・Claude Codeでは、利用するプロジェクトのルートに上記の配置先フォルダを作成し、リンク先のファイルを`SKILL.md`という名前で保存してください。両環境で同じファイルを使います。

詳細な手順と対応環境の注意は[導入ガイド](docs/installation.md)を参照してください。初回は[架空のサンプルPR](examples/sample-pr.md)で試せます。

## チームで使う

「このPR、AI家庭教師した？」「取得件数が増えるとSQL発行回数はどうなる？」と短い会話につなげます。詰まった箇所はAI家庭教師で学び直してもらいます。チームでAI家庭教師によるキャッチアップが当たり前の文化になるのが理想です。

客先では顧客のAI利用・情報共有ルールに従います。このリポジトリが公開されていることは、顧客コードをAIや公開Issueに入力してよいことを意味しません。

## フィードバックと改善

困った動作、学習体験、改善案はGitHubのIssuesから投稿できます。利用した版、AI環境・モデル、モード、期待と実際の差を記録してください。コードや会話は公開可能な架空の再現例を使います。実案件のコード・非公開PR URL・社名・個人情報・認証情報を貼らないでください。

投稿方法は[CONTRIBUTING.md](CONTRIBUTING.md)、改善の回し方は[保守ガイド](docs/maintenance.md)に記載しています。

## 開発

Python 3.11以上を使います。追加依存はありません。

```bash
python3 scripts/build.py
python3 scripts/check.py
```

家庭教師の共通仕様は`spec/ai-tutor.md`です。Skill・Copilot・Web UIの配布物を生成し、CIで更新漏れを検出します。最小プロンプトは要約版として別途維持します。生成物に直接修正を入れないでください。

## ライセンス

[MIT License](LICENSE)。商用利用・改変・再配布が可能です。所定の著作権表示と許諾文を保持してください。

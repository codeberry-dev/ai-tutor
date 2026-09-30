# 導入ガイド

確認日：2026-09-30。製品・バージョン・管理者設定により対応が異なります。

## Codex

リポジトリから`skills/ai-tutor/`フォルダ全体をコピーし、利用対象プロジェクトの`.agents/skills/ai-tutor/SKILL.md`に配置します。個人のローカルCodexでは`~/.agents/skills/ai-tutor/`も選べます。認識後に対象コードを指定して`$ai-tutor`を呼び出します。ChatGPTのSkillsへの登録は利用環境のインポート操作に従い、ローカル配置と同じ操作だと決めつけないでください。

## Claude Code

`skills/ai-tutor/`を対象プロジェクトの`.claude/skills/ai-tutor/`へコピーします。個人のローカル環境なら`~/.claude/skills/ai-tutor/`も使えます。対象を指定して`/ai-tutor`を実行します。プロジェクト配置はチーム共有時の選択肢です。クラウドセッションはローカル個人フォルダを参照しない場合があります。

## GitHub Copilot／VS Code

Prompt file対応のチャットでは、`prompts/copilot/ai-tutor.prompt.md`を対象プロジェクトの`.github/prompts/ai-tutor.prompt.md`へコピーします。教材ファイルや差分を添付・選択し、チャットで`/ai-tutor`を選びます。観点だけ必要なら「レビュー支援モード」と追記します。

VS Codeの現行文書ではPrompt filesはLocal agentで利用でき、Agent Hostセッションでは読まれません。Agent Hostを使う場合は、公式の移行案内とSkills対応を確認し、配布Skillの導入またはWeb用プロンプトの貼り付けを選んでください。他のCopilot IDEで同じコマンドが使えるとは限らないため、各IDEの公式手順を確認してください。常時適用するInstructionsには登録しません。

## Web UI

1. 新しい開発・学習チャットを開始する。
2. `prompts/web/ai-tutor.webui.md`の全文を一度送信する。登録時は授業を開始しない。
3. 普段どおり作業・相談する。
4. 「今回の変更についてAI家庭教師」と送る。
5. 観点だけなら「AI家庭教師 レビュー支援モード」と送る。

同じチャットでは通常、再貼り付けは不要です。新しいチャットでは再設定します。長い会話で指示が保持されていない場合も再送してください。URLだけではAIが本文を読めないことがあります。その場合は許可された範囲の抜粋または架空の再現例を使ってください。

## 制約がある客先

ファイルの配置・リポジトリへのコミットは顧客のルールに従ってください。配置ができても、AIへのコード入力が許可されるとは限りません。配置不可・貼り付け可なら最小プロンプトを使います。AI利用自体が禁止なら利用しません。

## 更新と利用版の記録

利用者はReleasesのタグと`VERSION`を記録し、必要な配布物を更新します。フィードバックにはその版を記載してください。古い版を実案件で使う必要があれば、タグの内容を使い、mainの変更と混同しないでください。

## 公式参照先

- [Codex／Skillの配置場所](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [VS Code Prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files)

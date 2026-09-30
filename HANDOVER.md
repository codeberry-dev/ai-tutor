# AI家庭教師：公開・保守引き継ぎ

## 目的と決定事項

コードベリーの社内運用で作成した「AI家庭教師」を、客先でも利用できるPublic GitHubプロジェクトとして公開する。利用者からIssueでフィードバックを集め、継続改善する。

- 表示名：AI家庭教師、技術識別名・推奨リポジトリ名：ai-tutor。
- 公開先：会社Organization `codeberry-dev` のPublicリポジトリ `ai-tutor`（ユーザー確認済み）。
- ライセンス：ユーザーがMITを選択。
- セルフ家庭教師とレビュー支援の2モード。
- 分からないことを歓迎し、基礎説明・具体例・小さな実践・元教材への適用・自分の言葉で説明まで支援する。
- 自分の生成物以外に他人のPRも教材にできる。読めなければ推測せず、共有が許可された資料・架空例を使う。
- SESのPRが顧客納品物になり得るため、PR説明欄に社内AI利用フォーマットを追加しない。
- シニアはレビュー観点を短く抽出し、後輩に声をかける。シニア自身も学べる。

## 準備済み

README、MIT、導入手順、貢献ガイド、保守手順、Issueフォーム3種、PRテンプレート、共通仕様、生成スクリプト、配布物、構造検証CI、架空教材、対話評価シナリオ。

既存v2パッケージのSkillを基に共通仕様を作成した。後から個別作成されたCopilotファイルとv2同梱ファイルが同内容であることも確認した。公開版では共有仕様に統合し、Web登録時の待機、1ターン1問、根拠のないレビュー前提の回避、顧客ルールの遵守を補足した。

このプロジェクトは配布物のソースであり、利用環境へのインストールは別の操作である。

## 未完了

- 実際のAI環境での対話評価と初回Release。CIの整合性確認は対話評価の代わりにはならない。

公開先のOrganizationを確認してからリポジトリを作成する。個人アカウントへ公開先を変更しない。

## 2026-09-30の作業確認

- `python3 scripts/build.py`で配布物を再生成し、`python3 scripts/check.py`は成功。
- Gitをmainで初期化し、指定名義で初回コミットとpushを完了。originは`https://github.com/codeberry-dev/ai-tutor.git`。
- GitHub CLIの認証は有効。所属Organizationとして`codeberry-dev`を確認し、認証ユーザーは同Organizationのactiveなadmin。Publicリポジトリ作成を許可する設定も確認。
- 作成直前に既存リポジトリがないことを確認し、[Publicリポジトリ](https://github.com/codeberry-dev/ai-tutor)を作成。IssuesとActionsは有効。運用ラベル5種を確認。
- 初回[Validate CI](https://github.com/codeberry-dev/ai-tutor/actions/runs/36686265493)は成功。mainの直接push制限は未設定。
- 初回Releaseは対話評価待ちの[ドラフト](https://github.com/codeberry-dev/ai-tutor/releases/tag/untagged-359a3678448d21cc04a4)を作成済み。公開タグとReleaseの公開はまだ行わない。
- ユーザーが公開先`codeberry-dev/ai-tutor`とMITの`Copyright (c) 2026 Codeberry`を承認。Author／Committerは`SATOSHI CHIBA <satoshi.chiba@codeberry.co.jp>`と指定。
- `evals/scenarios.md`と架空教材の内容を確認。実際のAI環境での対話評価は未実施であり、静的チェック成功を学習効果の根拠とはしない。

## 次の作業への依頼例

「HANDOVER.mdとAGENTS.mdを読み、このai-tutorを会社Organization `<正確なログイン名>` のPublicリポジトリへ公開する作業を続けて。既存リポジトリがあれば内容を確認して衝突を避け、配布物を検証し、評価結果を記録して初回Releaseまで準備して。」

## 構成と検証

`spec/ai-tutor.md`を編集し、`python3 scripts/build.py`で配布物を生成する。`python3 scripts/check.py`で整合性と内部リンクを確認する。教え方を変えたら`evals/scenarios.md`の関連ケースを実際のAIで評価する。

## コミットの表記

公開履歴にAI作業者名、Co-authored-byの自動追記、AI署名は追加しない。Author／Committerは管理者指定の`SATOSHI CHIBA <satoshi.chiba@codeberry.co.jp>`を使う。GitHub側の監査ログ等はこの方針の対象外。コミットとPushは実施済み。

## 初回公開のCLI例

GitHub認証と会社での権限がある開発環境で、Organization名をユーザーの指定値に置き換える。既存のorigin・履歴を確認してから実行する。

```bash
gh repo create <ORG>/ai-tutor --public --source=. --remote=origin --push
```

初回公開は実施済み。この例を既存リポジトリに再実行しない。

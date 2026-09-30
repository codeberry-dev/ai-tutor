# 架空のPR：注文一覧の関連データ取得

すべて学習用の架空コードです。実案件の情報は含みません。

## 目的

注文10件に紐づく顧客名を返すAPIで、注文ごとに顧客取得していた処理をまとめる。

```diff
 List<Order> orders = orderRepository.findLatest(10);
+Set<Long> ids = orders.stream().map(Order::customerId).collect(toSet());
+Map<Long, Customer> customers = customerRepository.findByIds(ids);
 for (Order order : orders) {
-    Customer customer = customerRepository.findById(order.customerId());
+    Customer customer = customers.get(order.customerId());
     result.add(new OrderView(order.id(), customer.name()));
 }
```

## この教材での前提

`findLatest`はSQLを1回発行。`findById`も1回。`findByIds`はidsが空ならSQLなし、空でなければIN句のSQLを1回発行してIDをキーにしたMapを返す。顧客が存在しないIDのエントリは返さない。キャッシュはない。この前提は実システムに一般化しないこと。

## 呼び出し例

「このPRを自分も理解したい。AI家庭教師」

「このPRの技術会話で使う観点だけ5点以内。AI家庭教師 レビュー支援モード」

# goit-algo-fp
Final project in scope of Basic Algorithms and Data Structures module

## Аналіз Результатів Симуляції Кидання Кубиків

Результати мільйонної симуляції кидання двох кубиків методом Монте-Карло були аналізовані та порівняні з теоретичними імовірностями кожної суми від 2 до 12.

### Основні Висновки:
- Емпіричні імовірності отримані в ході симуляції дуже близькі до теоретично обрахованих імовірностей для всіх сум. Це вказує на високу точність і ефективність методу Монте-Карло при великій кількості ітерацій.
- Найвища ймовірність була зафіксована для суми 7, що співпадає з теоретичним розподілом ймовірностей.
- Мінімальні відхилення емпіричних значень від теоретичних спостерігаються у крайніх значеннях (сума 2 і 12), що також відповідає теоретичним очікуванням.

Цей аналіз яскраво демонструє, що метод Монте-Карло є потужним інструментом для апроксимації ймовірносних розподілів в статистичних експериментах, особливо коли вони проведені з великою кількістю ітерацій.

### Таблиця Порівняння Імовірностей:

| Сума | Теоретична Імовірність | Емпірична Імовірність |
|------|------------------------|-----------------------|
| 2    | 0.0278                 | 0.0276                |
| 3    | 0.0556                 | 0.0555                |
| 4    | 0.0833                 | 0.0836                |
| 5    | 0.1111                 | 0.1112                |
| 6    | 0.1389                 | 0.1388                |
| 7    | 0.1667                 | 0.1665                |
| 8    | 0.1389                 | 0.1391                |
| 9    | 0.1111                 | 0.1108                |
| 10   | 0.0833                 | 0.0832                |
| 11   | 0.0556                 | 0.0557                |
| 12   | 0.0278                 | 0.0281                |

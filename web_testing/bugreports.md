# Bug Reports

### Bug #1 — Ошибка при регистрации
**Severity:** Major  
**Steps to Reproduce:**
1. Перейти на https://shop.demoqa.com/my-account/
2. Ввести невалидный email `test@@gmail.com`
3. Нажать "Register"  
**Expected result:** Сообщение "Invalid email format"  
**Actual result:** Страница зависает без сообщения  
**Status:** Open  

---

### Bug #2 — Некорректный ответ при авторизации
**Severity:** Minor  
**Steps:**
1. Перейти на страницу логина
2. Ввести email `test@test.com` и неверный пароль
3. Нажать "Login"  
**Expected:** Сообщение "Invalid password"  
**Actual:** Ошибка 500 в консоли (DevTools → Network)
**Status:** Open

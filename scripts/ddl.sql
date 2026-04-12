CREATE TABLE users (
      2     user_id BIGINT UNSIGNED NOT NULL PRIMARY KEY COMMENT 'Уникальный идентификатор пользователя',
      3     first_name VARCHAR(100) NOT NULL COMMENT 'Имя пользователя',
      4     last_name VARCHAR(100) NOT NULL COMMENT 'Фамилия пользователя',
      5     is_bot BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'Флаг: является ли пользователь ботом',
      6     last_activity_time TIMESTAMP NOT NULL COMMENT 'Время последней активности пользователя',
      7     name VARCHAR(200) NOT NULL COMMENT 'Полное имя пользователя',
      8     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Дата и время создания записи',
      9     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Дата и время последнего обновления записи',
     10
     11     INDEX idx_last_activity (last_activity_time) COMMENT 'Индекс для поиска по времени активности'
     12 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Таблица пользователей';
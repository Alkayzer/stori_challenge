include .env
export
.PHONY: migrate-up migrate-down

migrate-up:
	@echo "Applying migrations..."
	mysql -u ${DB_USER} -p${DB_PASS} -h ${DB_HOST} ${DB_NAME} < ./database/migrations/migrate_up.sql
	@echo "Migrations applied successfully."

migrate-down:
	@echo "Reverting migrations..."
	mysql -u ${DB_USER} -p${DB_PASS} -h ${DB_HOST} ${DB_NAME} < ./database/migrations/migrate_down.sql
	@echo "Migrations reverted successfully."

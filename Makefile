run: ## Build and run the application
	docker-compose -f docker-compose.yml up --build -d

requirements: ## Update requirements.txt
	poetry export --without-hashes -f requirements.txt > requirements.txt
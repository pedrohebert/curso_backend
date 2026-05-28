all : run


docker:
	docker compose up -d


run: docker
	source .venv/bin/activate && uv run uvicorn app.main:app --reload

down:
	docker compose down

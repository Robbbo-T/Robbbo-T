.PHONY: gate lint

gate:
	python ci/gates/link_path_validator.py &&     	python ci/gates/fcr_enforcer.py

lint:
	pre-commit run --all-files || true

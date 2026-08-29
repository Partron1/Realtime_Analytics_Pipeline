README.md                 # short quickstart + links to docs
pipelines/
  streaming.py            # Beam streaming pipeline (Pub/Sub → transform → BigQuery)
publisher/
  simulator.py            # multi-device event simulator (publishes to Pub/Sub)
configs/
  dev.yaml                # example values for local/dev
  prod.yaml               # example values for prod
samples/
  air_quality_data.jsonl   # sample events for simulation
infra/
  terraform/
    main.tf
    variables.tf
    outputs.tf
docs/
  architecture.md
  runbook.md
dashboards/
  tableau/                # dashboard notes / connection instructions
scripts/
  run_local_emulator.sh
  deploy_dataflow.sh
tests/
  test_transforms.py
.gitignore
requirements.txt
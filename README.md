# Qiskit MaxCut Pattern

End-to-end Qiskit workflow:

1. Map classical input to quantum problem
2. Optimize for hardware
3. Execute with Qiskit primitives
4. Post-process result
5. Deploy as cloud API

Run locally:
python run_local.py

Run API:
uvicorn service.api:app --reload

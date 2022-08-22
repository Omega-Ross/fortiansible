import ansible.runner

runner = ansible.runner.Runner(
    pattern="addinterface.yaml"
)

print(runner)
import json

config_file = '/var/vcap/jobs/groundcrew/config/worker.json'

with open(config_file,'r') as f:
    config = json.load(f)

config["resource_types"].append(
"""
    { "type": "s3-iam", "image": "docker:///governmentpaas/s3-resource:111760326_build_on_dockerfile" }
    { "type": "semver-iam", "image": "docker:///governmentpaas/semver-resource:111760326_build_on_dockerfile" }
"""
)

with open(config_file,'w') as f:
    json.dump(config, f)

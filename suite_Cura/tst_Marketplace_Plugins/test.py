source(findFile("scripts", "init.py"))
source(findFile('scripts', 'python/bdd.py'))

setupHooks('../shared/scripts/bdd_hooks.py')
collectStepDefinitions('../shared/steps')

def main():
    testSettings.throwOnFailure = True
    runFeatureFile('test.feature')

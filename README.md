# Hello World Names Action

A GitHub Action that reads names from a YAML file and prints personalized greetings.

## Usage
You can either use [this template repository](https://github.com/matthew-kilpatrick/hello-world-template) to create a new repository with this action and config file, or can use the code below to add it to an existing repository.


```yaml
name: Greet People
on: workflow_dispatch

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      
      - name: Say Hello
        uses: matthew-kilpatrick/hello-world-action@main # a tag can be used instead of main to use a fixed version
        with:
          names-file: 'names.yml'
```

Alternatively, you can clone this repository, modify the example yml file (`cp names.yml.example names.yml`) and invoke the script directly (`python hello.py names.yml`).

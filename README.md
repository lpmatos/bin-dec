# Bin-Dec

This is a basic application built without purpose.

![Alt text](docs/CMD.png?raw=true "BinDec")

## Copyright (c)

Lucca Pessoa da Silva Matos (c) 2019 - **GitHub Repository**.

## Getting Started

To use this repository you need to make a **git clone**:

```
git clone --depth 1 https://github.com/lpmatos/bin-dec.git -b master
```

This will give access on your **local machine** to this project.

## Organization

* **/code** in this folder we have the **bindec** application.
* **/docs** is the directory where we have all documentation files.
* **docker-compose.yml** is the **Docker** container orchestrator.
* **Dockerfile** is a file used to set up your **Docker** environment.
* **Makefile** is a file containing a set of automation policies.
* **README.md** is an optional file. A human-readable **README** file.
* The files found in the project root are support files.

## Description

**Tier:** 1-Beginner

Binary is the number system all digital computers are based on.
Therefore it's important for developers to understand binary, or base 2,
mathematics. The purpose of Bin2Dec is to provide practice and
understanding of how binary calculations.

Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's
and 1's, in any sequence and then displays its decimal equivalent.

This challenge requires that the developer implementing it follow these
constraints:

-   Arrays may not be used to contain the binary digits entered by the user
-   Determining the decimal equivalent of a particular binary digit in the
    sequence must be calculated using a single mathematical function, for
    example the natural logarithm. It's up to you to figure out which function
    to use.

### User Stories

-   [x] User can enter up to 8 binary digits in one input field
-   [x] User must be notified if anything other than a 0 or 1 was entered
-   [x] User views the results in a single output field containing the decimal (base 10) equivalent of the binary number that was entered

### Bonus features

-   [x] User can enter a variable number of binary digits

### Useful links and resources

[Binary number system](https://en.wikipedia.org/wiki/Binary_number)

### Example projects

Try not to view this until you've developed your own solution:

-   [Binary to decimal conversion program for beginners](https://www.youtube.com/watch?v=YMIALQE26KQ)
-   [Binary to Decimal converter using React](https://github.com/email2vimalraj/Bin2Dec)
-   [Binary to Decimal converter with plain html, js and css](https://grfreire.github.io/Bin2Dec/)
-   [Binary to Decimal converter using Flutter & Dart](https://github.com/israelss/AppIdeasCollection/tree/master/Tier1/Bin2Dec)
-   [Live preview built with Flutter for Web](https://bin2dec.web.app/#/)

## Pre-Requisites

**Tools**
:---:
**Python**
**Docker**
**docker-compose**

## Containers

It's set at [docker-compose.yml](docker-compose.yml) all the **Containers** required for the application execution.

**Container** | **Description** | **Dockerfile**
:---: | :---: | :---:
bindec | **Alpine Python Container** | [Dockerfile](Dockerfile)

## Structure

**Components** | **Description** | **Tool**
:---: | :---: | :---:
python | **Language to create a script that convert bin to dec** | [Python](https://www.python.org/)
docker | **Docker aims create, test and implement applications in a separate environment from the original machine, called a container** | [Docker](https://docs.docker.com/)

## Running pip

The **pip** is a command line program. When you install **pip**, a **pip** command is added to your system, which can be run from the command prompt as follows:

```bash
$ pip <pip arguments>
```

If you cannot run the pip command directly (possibly because the location where it was installed isn't on your operating systems **PATH**) then you can run **pip** via the **Python** interpreter:

```bash
$ python -m pip <pip arguments>
```

On **Windows**, the py launcher can be used:

```bash
$ py -m pip <pip arguments>
```

## Installing Packages

### Pip

The **pip** supports installing from **PyPI**, version control, local projects, and directly from distribution files.

The most common scenario is to install from **PyPI** using Requirement specifiers.

```bash
$ pip install SomePackage            # latest version
$ pip install SomePackage==1.0.4     # specific version
$ pip install somePackage>=1.0.4     # minimum version
```

### Pipenv

**Pipenv** is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the **Python** world. **Windows** is a firsts-class citizen, in our world.

It automatically creates and manages a **virtualenv** for your projects, as well as adds/removes packages from your **Pipfile** as you install/uninstall packages. It also generates the ever-important **Pipfile.lock**, which is used to produce deterministic builds.

#### Installation

```bash
$ pip install pipenv
```

#### Create a TOML Spec Pipfile

You can build the **Pipfile** to specifying:

* Versions of a Package.
* Versions of **Python**.
* Basic configurations.

#### Pipenv Workflow

Clone/create project repository:

```bash
$ cd myproject
```

Install from **Pipfile**, if there is one:

```bash
$ pipenv install
```

Install from **Pipfile** dev:

```bash
$ pipenv install --dev
```

## Requirement File

**Requirement File** are files containing a list of items to be installed using **pip** install like so:

```bash
$ pip install -r requirements.txt
```

Logically, a **Requirement File** is just a list of **pip** install arguments placed in a file. Note that you should not rely on the items in the file being installed by **pip** in any particular order.

## Docker

### Building

Additional steps for the developer to build the project after some code changes.

To **Build** the image:

```
docker image build -t <IMAGE_NAME> -f <PATH_DOCKERFILE> <PATH_CONTEXT_DOCKERFILE>
```

or

```
docker image build -t <IMAGE_NAME> . (This context)
```

Explain:

* **IMAGE_NAME**:
    * Image **Name/Tag**.
* **PATH_DOCKERFILE**:
    * **Dockerfile** location.
    * Where is the full path to **Dockerfile** located?
* **PATH_CONTEXT_DOCKERFILE**:
    * **Dockerfile** context.
    * Where is the **Dockerfile**?

#### Run the Container with the image

* Running the **Container** in **Detached mode**/**Background**:

```
docker container run -d -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME>
```

* Running the **Container** in **Interactive mode**:

```
docker container run -it --rm --name <CONTAINER_NAME> -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME>
```

### Basic Commands

* Windows

```
winpty docker.exe run -it --rm <IMAGE_NAME> <COMMAND>
```

* Showing all local images:

```
docker images
```

or

```
docker image ls
```

* Showing all Active or Inactive **Containers**:

```
docker ps -a
```

* Showing all Active **Containers**:

```
docker ps
```

* Entering an Active **Container**:

```
docker exec -it <CONTAINER_ID> <COMMAND>
```

## Built with

- [Alpine](https://alpinelinux.org/)
- [Python](https://www.python.org/)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## How to contribute

1. Make a **Fork**.

2. Follow the project organization.

3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.

4. Make the **Commit**.

5. Open a **Pull Request**.

6. Wait for your pull request to be accepted.. 🚀

Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

## Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

## Contacts

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

---

* **Email**: luccapsm@gmail.com
* **Linkedin**: www.linkedin.com/in/lucca-pessoa-4abb71138/

---

[![Facebook](https://github.frapsoft.com/social/facebook.png)](https://www.facebook.com/lucca.pessoa.9)
[![Github](https://github.frapsoft.com/social/github.png)](https://github.com/lpmatos)

## Versioning

- [CHANGELOG](CHANGELOG.md)

## Project Status

* In production

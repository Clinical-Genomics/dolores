# dolores

dolores :robot: is the API for all information that is necessary for automation at clinical genomics.

Dolores is a service that replaces the previous StatusDB in CG and wraps the database in a REST API.
All contacts with the business logic such as samples, cases etc will be done via this package.

## development
Make sure you have poetry installed

```
git clone https://github.com/Clinical-Genomics/dolores
cd dolores
# create your virtual env
poetry install
```
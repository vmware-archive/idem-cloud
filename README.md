# idem-cloud
Contracts for cloud providers built on POP and idem

# implementation
How to implement this contract in your cloud provider:
* Include `idem-cloud` in your requirements.txt
* Create functions in your cloud provider that use the same name and location of contracted functions in `idem-cloud`

For example, `idem-cloud.states.compute.contracts.virtual_machine.py` contains this contract:

```python
def sig_present(hub, ctx, name: str, provider: str, **kwargs):
    pass
```

In `your-cloud-provider.states.compute.virtual_machine.py` create a function that uses *at least* the same args and 
kwargs as the contract, this is an example from azurerm:

```python
async def present(hub, ctx, name, resource_group, tags=None, connection_auth=None, **kwargs):
    ...
```

Now you can create states with `idem-cloud` using `your-cloud-provider` as the `provider`.
Idem cloud will make sure that the typing and existence of your function args and kwargs are enforced.

This is the function in `idem-cloud.states.compute.virtual_machine.py` that calls your cloud provider's function:

```python
async def present(hub, ctx, name: str, provider: str, **kwargs):
    return await getattr(hub, f'states.{provider}.compute.virtual_machine')(ctx, name, **kwargs)
```

# How to Contribute
Many cloud providers will have similar functions and arguments.
`idem-cloud` keeps the APIs of all the different cloud providers as similar as possible.
Here are some pointers for creating a new contract:
* when creating a new contract, keep it as simple as possible. 
* Include only the *absolutely necessary* args and kwargs.
* Make use of Python3's `typing` module on function parameters.
* Read https://pop.readthedocs.io/en/latest/topics/contracts.html

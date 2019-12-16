# idem-cloud
Contracts for cloud providers built on POP and idem

# How to implement this contract in your cloud provider
* Include `idem-cloud` in your requirements.txt
* Create functions in your cloud that use the same name and location of functions in `idem-cloud`
    ```
    async def present(hub, ctx, name: str, provider: str, **kwargs):
        return await getattr(hub, f'states.{provider}.compute.virtual_machine')(ctx, name, **kwargs)
    ```

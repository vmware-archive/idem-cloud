async def present(hub, ctx, name: str, provider: str, **kwargs):
    return await getattr(hub, f'states.{provider}.compute.virtual_machine')(ctx, name, **kwargs)


async def absent(hub, ctx, name: str, provider: str, **kwargs):
    return await getattr(hub, f'states.{provider}.compute.virtual_machine')(ctx, name, **kwargs)

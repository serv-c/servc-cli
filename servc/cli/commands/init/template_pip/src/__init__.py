
def health_check(*args, **kwargs):
    return {"status": "ok"}


resolvers = {
    "healthCheck": health_check,
}

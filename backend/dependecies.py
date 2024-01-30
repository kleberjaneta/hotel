from fastapi import Header, HTTPException
from typing_extensions import Annotated


# async def validate_token_header(
#     Authorization: str = Header(),
# ) -> UserToken:
#     try:
#         authorization_token = Authorization.split(" ")[1]
#         # print("el token de autorizacion es este: ", authorization_token)

#         if not authorization_token:
#             raise HTTPException(status_code=400, detail="Token is missing")

#         current_user = auth_token.decode_access_token(authorization_token)
#         # print("el current user es: ", current_user)

#         # if current_user == None:  # el token no es valido
#         if not current_user:  # el token no es valido
#             raise HTTPException(status_code=404, detail="Session not found")

#         user_token = UserToken(**current_user)
#         # print(type(current_user))
#         # print(current_user.user_id)
#         # print(type(user_token))
#         # print(user_token)
#         return user_token
#     except Exception as e:
#         # print(e)
#         raise HTTPException(status_code=400, detail="Token is missing")


async def verify_key(x_key: Annotated[str, Header()], test: str | None = None):
    print("dependencie", x_key)
    print("dependency", test)

    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

import datetime
import config
import jwt


def encode_token(payload):
    payload['iat'] = datetime.datetime.utcnow()
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    token = jwt.encode(
        payload=payload,
        key=config.JWT_SECRET,
        algorithm='HS256',)
    return token


def decode_token(token):
    try:
        decoded = jwt.decode(
            token,
            config.JWT_SECRET,
            algorithms=['HS256'],)

        if datetime.datetime.utcnow() > datetime.datetime.fromtimestamp(decoded['exp']):
            raise jwt.ExpiredSignatureError("Token has expired")

        return decoded

    except jwt.ExpiredSignatureError:
        return "Token has expired."

    except jwt.InvalidTokenError:
        print("Invalid token.")
        return None

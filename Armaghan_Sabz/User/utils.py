
from Armaghan_Sabz.settings import  Kavenegar_KEY
from random import randint
from kavenegar import *
from .models import Profile


# make code for phone_number
def make_verification_code(phone_number , token):
    # code = str(randint(10000,99999))
    code = token
    pn = phone_number
    # rdis.set(pn, code, 120 )
    print('code is :', code)

    try:
      
                # test api with mykey(kimiya)
        # api = KavenegarAPI('514E6D347148396A577234665748586B58484644477748524432497338524B6E41573334485A4E683845303D')
        
        api = KavenegarAPI('616D734A466F564151424C36314F4865494263565742743955584E525739706F4C324E4758567868496B303D')
        params = {
            'sender': '1000596446',#optional
            'receptor': '+98' + str(pn),#multiple mobile number, split by comma
            'message': 'Wellcome to Armaghan Sabz your verification code is ' + str(code),
        } 
        response = api.sms_send(params)
        print(response)

    except APIException as e: 
        print(e)

    except HTTPException as e: 
        print(e)


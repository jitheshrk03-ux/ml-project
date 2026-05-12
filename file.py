import joblib

def fun_joblib('model'):
    model=joblib.dump(model,'model_joblib')
    return model

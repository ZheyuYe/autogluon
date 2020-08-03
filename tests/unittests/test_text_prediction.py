from autogluon import TextPrediction as task
from autogluon.utils.tabular.utils.loaders import load_pd

test_hyperparameters = {
    'models': {
            'BertForTextPredictionBasic': {
                'search_space': {
                    'optimization.num_train_epochs': 1
                }
            }
    }
}


def verify_sst():
    train_data = load_pd.load('https://autogluon-text.s3-accelerate.amazonaws.com/'
                              'glue/sst/train.parquet')
    dev_data = load_pd.load('https://autogluon-text.s3-accelerate.amazonaws.com/'
                            'glue/sst/dev.parquet')
    train_data = train_data.iloc[:100]
    dev_data = dev_data.iloc[:10]
    predictor = task.fit(train_data, hyperparameters=test_hyperparameters,
                         label='label', num_trials=1,
                         verbosity=4,
                         output_directory='./sst')
    dev_acc = predictor.evaluate(dev_data, metrics=['acc'])
    dev_prediction = predictor.predict(dev_data)
    dev_pred_prob = predictor.predict_proba(dev_data)


def verify_mrpc():
    train_data = load_pd.load(
        'https://autogluon-text.s3-accelerate.amazonaws.com/glue/mrpc/train.parquet')
    dev_data = load_pd.load(
        'https://autogluon-text.s3-accelerate.amazonaws.com/glue/mrpc/dev.parquet')
    train_data = train_data.iloc[:100]
    dev_data = dev_data.iloc[:10]
    predictor = task.fit(train_data, hyperparameters=test_hyperparameters,
                         label='label', num_trials=1, verbosity=4,
                         output_directory='./mrpc')
    dev_acc = predictor.evaluate(dev_data, metrics=['acc'])
    dev_prediction = predictor.predict(dev_data)
    dev_pred_prob = predictor.predict_proba(dev_data)


def verify_sts():
    train_data = load_pd.load(
        'https://autogluon-text.s3-accelerate.amazonaws.com/glue/sts/train.parquet')
    dev_data = load_pd.load(
        'https://autogluon-text.s3-accelerate.amazonaws.com/glue/sts/dev.parquet')
    train_data = train_data.iloc[:100]
    dev_data = dev_data.iloc[:10]
    predictor = task.fit(train_data, hyperparameters=test_hyperparameters,
                         label='score', num_trials=1,
                         verbosity=4,
                         output_directory='./sts')
    dev_rmse = predictor.evaluate(dev_data, metrics=['rmse'])
    dev_prediction = predictor.predict(dev_data)


def test_fit():
    verify_sst()
    # verify_sts()
    # verify_mrpc()

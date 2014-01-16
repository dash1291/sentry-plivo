from setuptools import setup


setup(
    name='sentry-plivo',
    version='0.1',
    author='Ashish Dubey',
    author_email='ashish.dubey91@gmail.com',
    url='https://github.com/dash1291/sentry-plivo',
    description='A Sentry plugin for sending SMS notifications via Plivo.',
    license='MIT',
    zip_safe=False,
    install_requires=[
        'sentry',
        'plivo'
    ],
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'plivo = sentry_plivo',
        ],
        'sentry.plugins': [
            'plivo = sentry_plivo.plugin:PlivoPlugin',
        ]
    }
)

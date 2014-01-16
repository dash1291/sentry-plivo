sentry-plivo
------------

Sentry plugin for SMS notifications via Plivo.

Installation
============

``pip install -e git+https://github.com/dash1291/sentry-plivo.git``

After installation, make sure to enable the ``Plivo`` plugin from ``Settings->Manage Integrations``.

Configuration
=============

After the plugin has been enabled you'll be required to configure it. You will need to input the ``Authentication ID`` and ``Authentication Token`` that can be obtained by registering an app on Plivo_.

.. _Plivo: http://plivo.com/

You will also be required to input the sender and recipient phone numbers that will be used while sending the SMS notifications.
FROM python:2.7.12
RUN pip install redis==2.10.5
RUN useradd -ms /bin/bash alpha
USER alpha
WORKDIR ./pyfiles
CMD ["python","sum.py"]
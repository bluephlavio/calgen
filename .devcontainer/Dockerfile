# Devcontainer Dockerfile for calgen
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install uv (Python dependency manager)
RUN pip install uv

# Install minimal TeX Live (for LaTeX)
RUN apt-get update && \
    apt-get install -y --no-install-recommends texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


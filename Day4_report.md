# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Бақытбек Мирас Жасуланұлы
- Group: IB-23-5b
- Token: D1-IB-23-5b-02-B7C2
- Repo: https://github.com/dwcwdcec/devnet-day1-IB-23-5b-miras

---

## 2) Evidence checklist (files exist)

### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt  
- artifacts/day4/docker/sampleapp_token_proof.txt  
- artifacts/day4/docker/sampleapp_docker_ps.txt  
- artifacts/day4/docker/sampleapp_build_log.txt  

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt  
- artifacts/day4/jenkins/buildapp_console.txt  
- artifacts/day4/jenkins/testapp_console.txt  
- artifacts/day4/jenkins/pipeline_script.groovy  
- artifacts/day4/jenkins/pipeline_console.txt  
- artifacts/day4/jenkins/jenkins_url.txt  

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt  
- artifacts/day4/ansible/ansible_hello.txt  
- artifacts/day4/ansible/ansible_playbook_install.txt  
- artifacts/day4/ansible/ports_conf_after.txt  
- artifacts/day4/ansible/curl_apache_8081.txt  

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt  
- artifacts/day4/security/login_v1.txt  
- artifacts/day4/security/signup_v2.txt  
- artifacts/day4/security/login_v2.txt  
- artifacts/day4/security/db_tables.txt  
- artifacts/day4/security/db_user_hash_sample.txt  

---

## 3) Commands output

```text
$ python src/day4_summary_builder.py
Summary generated successfully.

$ pytest -q
Tests completed.

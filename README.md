### Network Security Projects for Phising Data
This repository contains a dataset designed for training and evaluating machine learning models that detect spam / phishing network activity based on URL and domain-related features.

### Overview
Each row in the dataset corresponds to one URL, with features encoded as:

1 → legitimate / safe

0 → suspicious / borderline

–1 → malicious / unsafe

| Feature Name                  | Description                                                          |
| ----------------------------- | -------------------------------------------------------------------- |
| `having_IP_Address`           | Whether the URL contains an IP address instead of a domain name.     |
| `URL_Length`                  | Categorized length of the URL (long URLs often indicate phishing).   |
| `Shortining_Service`          | Whether the URL uses a shortening service (bit.ly, tinyurl, etc.).   |
| `having_At_Symbol`            | Presence of "@" symbol in URL — often used to trick users.           |
| `double_slash_redirecting`    | Use of multiple "//" for redirection.                                |
| `Prefix_Suffix`               | Presence of dash (“-”) in domain part.                               |
| `having_Sub_Domain`           | Number of subdomains used (more subdomains often indicate phishing). |
| `SSLfinal_State`              | Validity and trustworthiness of SSL certificate.                     |
| `Domain_registeration_length` | Duration of domain registration.                                     |
| `Favicon`                     | Whether favicon loads from external or suspicious sources.           |
| `port`                        | Usage of non-standard ports.                                         |
| `HTTPS_token`                 | Use of misleading "HTTPS" tokens in domain.                          |
| `Request_URL`                 | Ratio of external object requests (images, scripts).                 |
| `URL_of_Anchor`               | Percentage of suspicious anchors referencing external domains.       |
| `Links_in_tags`               | Suspicious links in `<meta>`, `<script>`, and `<link>` elements.     |
| `SFH`                         | Server Form Handler analysis.                                        |
| `Submitting_to_email`         | Whether forms submit data to an email address.                       |
| `Abnormal_URL`                | URL not matching domain records.                                     |
| `Redirect`                    | Number of redirects.                                                 |
| `on_mouseover`                | Malicious JavaScript triggered by hovering.                          |
| `RightClick`                  | Disabled right-click functionality (common in phishing sites).       |
| `popUpWidnow`                 | Use of popup windows.                                                |
| `Iframe`                      | Use of invisible `<iframe>` elements.                                |
| `age_of_domain`               | Domain age (younger domains are often suspicious).                   |
| `DNSRecord`                   | Missing or inconsistent DNS records.                                 |
| `web_traffic`                 | Website ranking and traffic.                                         |
| `Page_Rank`                   | PageRank score of the domain.                                        |
| `Google_Index`                | Whether the site is indexed by Google.                               |
| `Links_pointing_to_page`      | Number of inbound links.                                             |
| `Statistical_report`          | Statistical data from blacklists and reputation services.            |

# Meridian Private Cloud: High-Level Design (SYNTHETIC)

## Page 1: Document control [cover]

- (F00001) Document HLD-859 version 2.3 is owned by Network Operations, reviewed on 2026-12-04, classified Internal and applies to Eastvale and Dunmoor.

- (F00002) Document HLD-130 version 0.3 is owned by Network Operations, reviewed on 2028-10-01, classified Internal and applies to Fernhollow and Fernhollow.

- (F00003) Assumption A-070: Dunmoor provides 2 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

- (F00004) Document HLD-877 version 1.6 is owned by Infrastructure Architecture, reviewed on 2027-03-07, classified Confidential and applies to Aldermere and Aldermere.

- (F00005) Requirement R-050: the batch tier must tolerate loss of one rack with recovery inside 60 minutes and no more than 0 minutes of data loss.

- (F00006) Assumption A-059: Eastvale provides 2 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00007) Assumption A-038: Fernhollow provides 4 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Network Operations.

- (F00008) Assumption A-009: Aldermere provides 4 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

- (F00009) Document HLD-975 version 1.1 is owned by Service Delivery, reviewed on 2027-08-21, classified Confidential and applies to Brightholm and Cresswick.

## Page 2: Stakeholders [cover]

- (F00010) Document HLD-786 version 2.1 is owned by Network Operations, reviewed on 2028-12-08, classified Internal and applies to Dunmoor and Dunmoor.

- (F00011) Requirement R-328: the cache tier must tolerate loss of one site with recovery inside 60 minutes and no more than 0 minutes of data loss.

- (F00012) Document HLD-941 version 0.5 is owned by Service Delivery, reviewed on 2027-02-07, classified Confidential and applies to Brightholm and Fernhollow.

- (F00013) Requirement R-203: the monitoring tier must tolerate loss of one host with recovery inside 60 minutes and no more than 0 minutes of data loss.

- (F00014) Document HLD-862 version 2.9 is owned by Service Delivery, reviewed on 2028-07-12, classified Internal and applies to Brightholm and Eastvale.

- (F00015) Requirement R-047: the web tier must tolerate loss of one host with recovery inside 15 minutes and no more than 5 minutes of data loss.

- (F00016) Document HLD-911 version 3.9 is owned by Platform Engineering, reviewed on 2027-07-20, classified Confidential and applies to Eastvale and Cresswick.

- (F00017) Assumption A-111: Aldermere provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00018) Assumption A-114: Eastvale provides 3 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

## Page 3: Document control [cover]

- (F00019) Requirement R-223: the data tier must tolerate loss of one rack with recovery inside 5 minutes and no more than 5 minutes of data loss.

- (F00020) Assumption A-034: Eastvale provides 2 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00021) Assumption A-039: Fernhollow provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Network Operations.

- (F00022) Document HLD-482 version 1.8 is owned by Platform Engineering, reviewed on 2028-06-16, classified Internal and applies to Aldermere and Cresswick.

- (F00023) Requirement R-123: the web tier must tolerate loss of one host with recovery inside 5 minutes and no more than 0 minutes of data loss.

- (F00024) Assumption A-063: Aldermere provides 4 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Network Operations.

- (F00025) Assumption A-061: Eastvale provides 2 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00026) Document HLD-652 version 1.4 is owned by Service Delivery, reviewed on 2028-11-12, classified Confidential and applies to Eastvale and Dunmoor.

- (F00027) Document HLD-353 version 1.1 is owned by Infrastructure Architecture, reviewed on 2026-10-18, classified Internal and applies to Eastvale and Brightholm.

## Page 4: Document control [cover]

- (F00028) Document HLD-824 version 0.3 is owned by Platform Engineering, reviewed on 2026-06-03, classified Internal and applies to Cresswick and Fernhollow.

- (F00029) Requirement R-110: the data tier must tolerate loss of one site with recovery inside 240 minutes and no more than 0 minutes of data loss.

- (F00030) Requirement R-209: the cache tier must tolerate loss of one host with recovery inside 5 minutes and no more than 5 minutes of data loss.

- (F00031) Requirement R-182: the bastion tier must tolerate loss of one rack with recovery inside 240 minutes and no more than 5 minutes of data loss.

- (F00032) Document HLD-789 version 0.0 is owned by Service Delivery, reviewed on 2028-06-26, classified Internal and applies to Brightholm and Brightholm.

- (F00033) Document HLD-649 version 3.2 is owned by Service Delivery, reviewed on 2026-05-15, classified Internal and applies to Aldermere and Dunmoor.

- (F00034) Assumption A-013: Aldermere provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00035) Document HLD-871 version 1.2 is owned by Service Delivery, reviewed on 2027-08-07, classified Confidential and applies to Aldermere and Brightholm.

- (F00036) Requirement R-002: the bastion tier must tolerate loss of one rack with recovery inside 240 minutes and no more than 1 minutes of data loss.

## Page 5: Requirements [cover]

- (F00037) Assumption A-094: Eastvale provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00038) Document HLD-294 version 2.3 is owned by Platform Engineering, reviewed on 2028-12-18, classified Internal and applies to Fernhollow and Cresswick.

- (F00039) Document HLD-151 version 3.8 is owned by Network Operations, reviewed on 2026-09-03, classified Internal and applies to Aldermere and Eastvale.

- (F00040) Document HLD-791 version 1.6 is owned by Platform Engineering, reviewed on 2028-04-19, classified Internal and applies to Eastvale and Aldermere.

- (F00041) Requirement R-337: the batch tier must tolerate loss of one rack with recovery inside 15 minutes and no more than 5 minutes of data loss.

- (F00042) Assumption A-041: Brightholm provides 3 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Network Operations.

- (F00043) Assumption A-083: Cresswick provides 3 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00044) Document HLD-569 version 0.1 is owned by Network Operations, reviewed on 2028-05-05, classified Confidential and applies to Aldermere and Brightholm.

- (F00045) Requirement R-146: the data tier must tolerate loss of one rack with recovery inside 60 minutes and no more than 5 minutes of data loss.

## Page 6: Assumptions [cover]

- (F00046) Document HLD-783 version 2.1 is owned by Network Operations, reviewed on 2027-02-04, classified Internal and applies to Cresswick and Cresswick.

- (F00047) Assumption A-027: Fernhollow provides 3 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

- (F00048) Assumption A-063: Cresswick provides 2 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00049) Requirement R-023: the web tier must tolerate loss of one rack with recovery inside 15 minutes and no more than 5 minutes of data loss.

- (F00050) Requirement R-083: the monitoring tier must tolerate loss of one site with recovery inside 240 minutes and no more than 5 minutes of data loss.

- (F00051) Document HLD-214 version 0.2 is owned by Platform Engineering, reviewed on 2027-10-18, classified Internal and applies to Dunmoor and Brightholm.

- (F00052) Document HLD-415 version 2.0 is owned by Infrastructure Architecture, reviewed on 2026-11-08, classified Internal and applies to Cresswick and Eastvale.

- (F00053) Requirement R-318: the data tier must tolerate loss of one host with recovery inside 15 minutes and no more than 0 minutes of data loss.

- (F00054) Requirement R-013: the data tier must tolerate loss of one site with recovery inside 60 minutes and no more than 1 minutes of data loss.

## Page 7: Scope and objectives [cover]

- (F00055) Requirement R-082: the app tier must tolerate loss of one rack with recovery inside 5 minutes and no more than 1 minutes of data loss.

- (F00056) Document HLD-304 version 3.5 is owned by Infrastructure Architecture, reviewed on 2026-04-01, classified Internal and applies to Dunmoor and Cresswick.

- (F00057) Requirement R-036: the queue tier must tolerate loss of one rack with recovery inside 240 minutes and no more than 5 minutes of data loss.

- (F00058) Assumption A-043: Aldermere provides 2 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Network Operations.

- (F00059) Assumption A-034: Aldermere provides 2 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00060) Requirement R-374: the batch tier must tolerate loss of one rack with recovery inside 5 minutes and no more than 1 minutes of data loss.

- (F00061) Assumption A-025: Cresswick provides 2 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00062) Document HLD-632 version 1.5 is owned by Service Delivery, reviewed on 2026-11-11, classified Confidential and applies to Fernhollow and Aldermere.

- (F00063) Assumption A-116: Cresswick provides 4 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

## Page 8: Stakeholders [cover]

- (F00064) Requirement R-357: the queue tier must tolerate loss of one site with recovery inside 15 minutes and no more than 0 minutes of data loss.

- (F00065) Requirement R-341: the bastion tier must tolerate loss of one site with recovery inside 15 minutes and no more than 5 minutes of data loss.

- (F00066) Assumption A-039: Dunmoor provides 4 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

- (F00067) Requirement R-108: the bastion tier must tolerate loss of one site with recovery inside 60 minutes and no more than 1 minutes of data loss.

- (F00068) Requirement R-227: the cache tier must tolerate loss of one site with recovery inside 240 minutes and no more than 5 minutes of data loss.

- (F00069) Document HLD-774 version 0.4 is owned by Infrastructure Architecture, reviewed on 2026-04-22, classified Confidential and applies to Brightholm and Brightholm.

- (F00070) Document HLD-125 version 0.3 is owned by Service Delivery, reviewed on 2028-02-15, classified Confidential and applies to Fernhollow and Eastvale.

- (F00071) Document HLD-835 version 3.7 is owned by Service Delivery, reviewed on 2026-03-21, classified Internal and applies to Aldermere and Dunmoor.

- (F00072) Document HLD-280 version 3.0 is owned by Network Operations, reviewed on 2026-08-05, classified Confidential and applies to Fernhollow and Eastvale.

## Page 9: Assumptions [cover]

- (F00073) Assumption A-041: Dunmoor provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00074) Assumption A-058: Brightholm provides 4 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00075) Requirement R-385: the cache tier must tolerate loss of one site with recovery inside 60 minutes and no more than 5 minutes of data loss.

- (F00076) Requirement R-321: the cache tier must tolerate loss of one rack with recovery inside 240 minutes and no more than 0 minutes of data loss.

- (F00077) Assumption A-037: Brightholm provides 3 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

- (F00078) Assumption A-011: Brightholm provides 2 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00079) Assumption A-020: Fernhollow provides 2 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00080) Requirement R-170: the monitoring tier must tolerate loss of one rack with recovery inside 5 minutes and no more than 0 minutes of data loss.

- (F00081) Requirement R-200: the web tier must tolerate loss of one site with recovery inside 240 minutes and no more than 1 minutes of data loss.

## Page 10: Document control [cover]

- (F00082) Requirement R-153: the bastion tier must tolerate loss of one rack with recovery inside 15 minutes and no more than 1 minutes of data loss.

- (F00083) Document HLD-379 version 3.7 is owned by Platform Engineering, reviewed on 2027-06-22, classified Confidential and applies to Fernhollow and Brightholm.

- (F00084) Requirement R-066: the web tier must tolerate loss of one rack with recovery inside 5 minutes and no more than 0 minutes of data loss.

- (F00085) Assumption A-055: Brightholm provides 3 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00086) Requirement R-195: the batch tier must tolerate loss of one host with recovery inside 240 minutes and no more than 1 minutes of data loss.

- (F00087) Requirement R-390: the bastion tier must tolerate loss of one rack with recovery inside 240 minutes and no more than 1 minutes of data loss.

- (F00088) Document HLD-581 version 0.8 is owned by Platform Engineering, reviewed on 2027-04-21, classified Internal and applies to Fernhollow and Aldermere.

- (F00089) Document HLD-353 version 1.0 is owned by Network Operations, reviewed on 2026-03-16, classified Internal and applies to Eastvale and Brightholm.

- (F00090) Requirement R-359: the queue tier must tolerate loss of one rack with recovery inside 15 minutes and no more than 5 minutes of data loss.

## Page 11: Assumptions [cover]

- (F00091) Assumption A-092: Aldermere provides 2 diverse carrier paths and 25 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00092) Assumption A-004: Cresswick provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00093) Requirement R-367: the cache tier must tolerate loss of one host with recovery inside 15 minutes and no more than 0 minutes of data loss.

- (F00094) Assumption A-099: Cresswick provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00095) Assumption A-101: Aldermere provides 3 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00096) Assumption A-048: Aldermere provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

- (F00097) Document HLD-969 version 3.7 is owned by Platform Engineering, reviewed on 2027-06-21, classified Confidential and applies to Fernhollow and Brightholm.

- (F00098) Requirement R-091: the queue tier must tolerate loss of one site with recovery inside 240 minutes and no more than 1 minutes of data loss.

- (F00099) Requirement R-375: the queue tier must tolerate loss of one rack with recovery inside 15 minutes and no more than 0 minutes of data loss.

## Page 12: Stakeholders [cover]

- (F00100) Requirement R-125: the monitoring tier must tolerate loss of one site with recovery inside 240 minutes and no more than 1 minutes of data loss.

- (F00101) Document HLD-606 version 2.2 is owned by Service Delivery, reviewed on 2026-06-26, classified Confidential and applies to Cresswick and Cresswick.

- (F00102) Assumption A-090: Cresswick provides 4 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Network Operations.

- (F00103) Document HLD-347 version 3.7 is owned by Network Operations, reviewed on 2028-08-21, classified Confidential and applies to Dunmoor and Aldermere.

- (F00104) Document HLD-401 version 1.6 is owned by Network Operations, reviewed on 2027-11-19, classified Confidential and applies to Dunmoor and Eastvale.

- (F00105) Assumption A-045: Dunmoor provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

- (F00106) Requirement R-360: the monitoring tier must tolerate loss of one rack with recovery inside 60 minutes and no more than 1 minutes of data loss.

- (F00107) Document HLD-223 version 1.5 is owned by Platform Engineering, reviewed on 2028-09-25, classified Internal and applies to Brightholm and Brightholm.

- (F00108) Assumption A-062: Cresswick provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Infrastructure Architecture.

## Page 13: Document control [cover]

- (F00109) Document HLD-403 version 1.5 is owned by Network Operations, reviewed on 2027-01-23, classified Internal and applies to Cresswick and Aldermere.

- (F00110) Document HLD-666 version 2.2 is owned by Service Delivery, reviewed on 2026-01-19, classified Confidential and applies to Dunmoor and Dunmoor.

- (F00111) Requirement R-175: the data tier must tolerate loss of one host with recovery inside 60 minutes and no more than 1 minutes of data loss.

- (F00112) Document HLD-941 version 0.6 is owned by Service Delivery, reviewed on 2026-10-21, classified Internal and applies to Brightholm and Brightholm.

- (F00113) Assumption A-039: Aldermere provides 2 diverse carrier paths and 10 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00114) Assumption A-077: Eastvale provides 2 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Service Delivery.

- (F00115) Requirement R-227: the queue tier must tolerate loss of one site with recovery inside 240 minutes and no more than 1 minutes of data loss.

- (F00116) Assumption A-080: Aldermere provides 4 diverse carrier paths and 100 Gbit/s of committed bandwidth; any change is raised with Platform Engineering.

- (F00117) Document HLD-740 version 1.4 is owned by Platform Engineering, reviewed on 2026-04-06, classified Internal and applies to Brightholm and Aldermere.

## Page 14: Load balancing [network]

- (F00118) Load balancer pool ledger-preprod fronts 6 members with weighted balancing, health probe http/8080 every 10s and idle timeout 60s; persistence cookie.

- (F00119) Firewall rule 4241 permits udp/443 from 10.115.76.0/24 to 10.136.72.0/26 with full logging; the rule is reviewed every 30 days by Network Operations and expires on 2028-10-24.

- (F00120) BGP peering between core-5 (AS 65228) and edge-7 (AS 65477) at Cresswick uses timers 30/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-APP-20 applies.

- (F00121) VLAN 1125 (web-prod) is trunked between dun-sw24 and cre-sw20 on port-channel 15, uses MTU 9216, maps to VRF MGMT-1 and runs MSTP with bridge priority 4096; changes require CAB approval 4 days ahead.

- (F00122) Load balancer pool scheduler-mgmt fronts 8 members with weighted balancing, health probe http/80 every 10s and idle timeout 300s; persistence source-ip.

- (F00123) BGP peering between core-6 (AS 64933) and edge-8 (AS 64807) at Fernhollow uses timers 10/90s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-APP-11 applies.

- (F00124) BGP peering between core-1 (AS 65185) and edge-8 (AS 64935) at Aldermere uses timers 3/90s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-MONITORING-21 applies.

- (F00125) Load balancer pool scheduler-test fronts 9 members with weighted balancing, health probe http/80 every 5s and idle timeout 240s; persistence cookie.

- (F00126) Firewall rule 7684 permits tcp/8443 from 10.58.236.0/24 to 10.60.78.0/26 with drop-only logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2028-08-16.

## Page 15: Switching fabric [network]

- (F00127) Load balancer pool scheduler-prod fronts 6 members with round-robin balancing, health probe http/8080 every 10s and idle timeout 60s; persistence source-ip.

- (F00128) BGP peering between core-3 (AS 64969) and edge-8 (AS 64865) at Cresswick uses timers 30/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-BATCH-28 applies.

- (F00129) Firewall rule 4826 permits udp/443 from 10.162.242.0/24 to 10.195.197.0/26 with sampled logging; the rule is reviewed every 60 days by Service Delivery and expires on 2027-03-17.

- (F00130) BGP peering between core-8 (AS 64527) and edge-3 (AS 64931) at Fernhollow uses timers 3/9s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-BATCH-20 applies.

- (F00131) Load balancer pool reports-test fronts 12 members with weighted balancing, health probe http/8080 every 5s and idle timeout 60s; persistence none.

- (F00132) BGP peering between core-2 (AS 65290) and edge-2 (AS 64966) at Brightholm uses timers 30/30s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-BATCH-26 applies.

- (F00133) VLAN 696 (cache-mgmt) is trunked between cre-sw12 and cre-sw14 on port-channel 27, uses MTU 9216, maps to VRF PREPROD-3 and runs RSTP with bridge priority 4096; changes require CAB approval 8 days ahead.

- (F00134) Firewall rule 8555 permits udp/1433 from 10.130.4.0/24 to 10.238.147.0/26 with sampled logging; the rule is reviewed every 60 days by Platform Engineering and expires on 2028-06-19.

- (F00135) BGP peering between core-8 (AS 65377) and edge-5 (AS 64715) at Dunmoor uses timers 10/9s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-BATCH-19 applies.

## Page 16: Perimeter firewalls [network]

- (F00136) BGP peering between core-1 (AS 65091) and edge-1 (AS 65444) at Eastvale uses timers 30/30s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-BATCH-8 applies.

- (F00137) Firewall rule 3240 permits tcp/6379 from 10.20.158.0/24 to 10.225.17.0/26 with sampled logging; the rule is reviewed every 90 days by Network Operations and expires on 2027-05-11.

- (F00138) Load balancer pool mailer-mgmt fronts 10 members with round-robin balancing, health probe tcp/443 every 10s and idle timeout 300s; persistence cookie.

- (F00139) BGP peering between core-4 (AS 65392) and edge-7 (AS 65502) at Eastvale uses timers 10/9s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-QUEUE-18 applies.

- (F00140) VLAN 2853 (queue-mgmt) is trunked between dun-sw12 and fer-sw24 on port-channel 25, uses MTU 9216, maps to VRF TEST-2 and runs RSTP with bridge priority 32768; changes require CAB approval 2 days ahead.

- (F00141) BGP peering between core-8 (AS 65443) and edge-5 (AS 65176) at Dunmoor uses timers 3/9s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-QUEUE-16 applies.

- (F00142) VLAN 1691 (monitoring-test) is trunked between ald-sw08 and eas-sw05 on port-channel 43, uses MTU 9216, maps to VRF MGMT-7 and runs RSTP with bridge priority 32768; changes require CAB approval 3 days ahead.

- (F00143) Load balancer pool mailer-preprod fronts 9 members with round-robin balancing, health probe tcp/443 every 5s and idle timeout 300s; persistence cookie.

- (F00144) BGP peering between core-2 (AS 65483) and edge-8 (AS 64605) at Fernhollow uses timers 3/90s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-WEB-2 applies.

## Page 17: Perimeter firewalls [network]

- (F00145) Firewall rule 4394 permits tcp/8443 from 10.168.75.0/24 to 10.1.141.0/26 with full logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2027-02-22.

- (F00146) VLAN 2511 (batch-prod) is trunked between bri-sw01 and cre-sw08 on port-channel 12, uses MTU 9000, maps to VRF PROD-3 and runs MSTP with bridge priority 4096; changes require CAB approval 3 days ahead.

- (F00147) Load balancer pool catalogue-dr fronts 10 members with least-connections balancing, health probe https/80 every 30s and idle timeout 300s; persistence source-ip.

- (F00148) VLAN 2910 (app-dr) is trunked between ald-sw16 and dun-sw14 on port-channel 46, uses MTU 9000, maps to VRF PROD-2 and runs MSTP with bridge priority 8192; changes require CAB approval 3 days ahead.

- (F00149) Firewall rule 9984 permits udp/1433 from 10.150.232.0/24 to 10.220.50.0/26 with sampled logging; the rule is reviewed every 30 days by Network Operations and expires on 2028-08-08.

- (F00150) Load balancer pool catalogue-test fronts 8 members with round-robin balancing, health probe https/443 every 10s and idle timeout 240s; persistence cookie.

- (F00151) Load balancer pool reports-prod fronts 7 members with least-connections balancing, health probe https/80 every 30s and idle timeout 300s; persistence cookie.

- (F00152) VLAN 3655 (web-test) is trunked between dun-sw12 and fer-sw14 on port-channel 39, uses MTU 9000, maps to VRF TEST-2 and runs RSTP with bridge priority 8192; changes require CAB approval 9 days ahead.

- (F00153) Firewall rule 2882 permits udp/9092 from 10.115.219.0/24 to 10.13.136.0/26 with full logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2029-05-11.

## Page 18: Perimeter firewalls [network]

- (F00154) VLAN 1741 (app-preprod) is trunked between bri-sw05 and eas-sw22 on port-channel 48, uses MTU 9216, maps to VRF PROD-2 and runs RSTP with bridge priority 32768; changes require CAB approval 8 days ahead.

- (F00155) Load balancer pool mailer-mgmt fronts 11 members with least-connections balancing, health probe tcp/80 every 5s and idle timeout 60s; persistence cookie.

- (F00156) VLAN 2089 (monitoring-dr) is trunked between cre-sw15 and fer-sw14 on port-channel 18, uses MTU 1500, maps to VRF MGMT-2 and runs MSTP with bridge priority 32768; changes require CAB approval 3 days ahead.

- (F00157) BGP peering between core-5 (AS 64558) and edge-4 (AS 64916) at Eastvale uses timers 3/9s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-CACHE-25 applies.

- (F00158) Firewall rule 1126 permits udp/6379 from 10.220.89.0/24 to 10.66.194.0/26 with sampled logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2027-07-28.

- (F00159) VLAN 3631 (batch-mgmt) is trunked between dun-sw01 and dun-sw03 on port-channel 28, uses MTU 9216, maps to VRF DR-7 and runs MSTP with bridge priority 4096; changes require CAB approval 8 days ahead.

- (F00160) VLAN 3507 (batch-prod) is trunked between cre-sw06 and eas-sw15 on port-channel 28, uses MTU 1500, maps to VRF PREPROD-7 and runs MSTP with bridge priority 4096; changes require CAB approval 8 days ahead.

- (F00161) BGP peering between core-3 (AS 64590) and edge-2 (AS 65055) at Eastvale uses timers 3/30s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-DATA-8 applies.

- (F00162) VLAN 2567 (data-prod) is trunked between bri-sw09 and bri-sw06 on port-channel 12, uses MTU 9216, maps to VRF DR-8 and runs MSTP with bridge priority 24576; changes require CAB approval 7 days ahead.

## Page 19: Switching fabric [network]

- (F00163) Load balancer pool telemetry-test fronts 11 members with least-connections balancing, health probe http/8080 every 5s and idle timeout 300s; persistence source-ip.

- (F00164) Load balancer pool catalogue-prod fronts 11 members with weighted balancing, health probe https/443 every 10s and idle timeout 60s; persistence source-ip.

- (F00165) Firewall rule 3471 permits tcp/1433 from 10.52.175.0/24 to 10.43.88.0/26 with full logging; the rule is reviewed every 60 days by Service Delivery and expires on 2028-09-17.

- (F00166) Firewall rule 7697 permits udp/6379 from 10.26.171.0/24 to 10.33.168.0/26 with full logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2028-12-28.

- (F00167) Firewall rule 3317 permits udp/5432 from 10.200.66.0/24 to 10.43.158.0/26 with sampled logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2027-11-23.

- (F00168) VLAN 1582 (web-test) is trunked between fer-sw22 and dun-sw17 on port-channel 20, uses MTU 1500, maps to VRF PREPROD-6 and runs MSTP with bridge priority 8192; changes require CAB approval 5 days ahead.

- (F00169) Firewall rule 9317 permits tcp/6379 from 10.172.67.0/24 to 10.192.78.0/26 with full logging; the rule is reviewed every 60 days by Network Operations and expires on 2029-08-02.

- (F00170) Load balancer pool identity-mgmt fronts 6 members with weighted balancing, health probe http/80 every 30s and idle timeout 240s; persistence source-ip.

- (F00171) Load balancer pool identity-dr fronts 6 members with round-robin balancing, health probe https/8080 every 10s and idle timeout 240s; persistence none.

## Page 20: WAN links [network]

- (F00172) Firewall rule 7081 permits tcp/6379 from 10.63.145.0/24 to 10.42.82.0/26 with drop-only logging; the rule is reviewed every 180 days by Network Operations and expires on 2028-02-08.

- (F00173) Load balancer pool reports-mgmt fronts 7 members with least-connections balancing, health probe http/80 every 10s and idle timeout 240s; persistence none.

- (F00174) BGP peering between core-3 (AS 64652) and edge-1 (AS 64805) at Dunmoor uses timers 30/9s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-MONITORING-20 applies.

- (F00175) VLAN 3520 (data-mgmt) is trunked between ald-sw01 and cre-sw07 on port-channel 47, uses MTU 9216, maps to VRF MGMT-7 and runs RSTP with bridge priority 24576; changes require CAB approval 5 days ahead.

- (F00176) BGP peering between core-8 (AS 64576) and edge-2 (AS 65368) at Dunmoor uses timers 30/90s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-CACHE-23 applies.

- (F00177) Firewall rule 6780 permits tcp/9092 from 10.213.95.0/24 to 10.43.184.0/26 with full logging; the rule is reviewed every 30 days by Service Delivery and expires on 2028-01-21.

- (F00178) Load balancer pool mailer-prod fronts 7 members with least-connections balancing, health probe https/8080 every 30s and idle timeout 60s; persistence cookie.

- (F00179) BGP peering between core-6 (AS 65345) and edge-3 (AS 65362) at Fernhollow uses timers 10/90s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-DATA-26 applies.

- (F00180) Firewall rule 5807 permits tcp/443 from 10.102.21.0/24 to 10.161.158.0/26 with sampled logging; the rule is reviewed every 180 days by Service Delivery and expires on 2028-01-25.

## Page 21: Switching fabric [network]

- (F00181) BGP peering between core-5 (AS 64639) and edge-6 (AS 64959) at Dunmoor uses timers 30/30s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-DATA-16 applies.

- (F00182) Load balancer pool reports-prod fronts 8 members with weighted balancing, health probe tcp/8080 every 10s and idle timeout 300s; persistence none.

- (F00183) VLAN 1926 (bastion-preprod) is trunked between cre-sw22 and cre-sw10 on port-channel 45, uses MTU 9000, maps to VRF TEST-8 and runs RSTP with bridge priority 24576; changes require CAB approval 8 days ahead.

- (F00184) BGP peering between core-7 (AS 64884) and edge-3 (AS 65487) at Aldermere uses timers 3/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-WEB-5 applies.

- (F00185) VLAN 1668 (web-mgmt) is trunked between bri-sw21 and cre-sw12 on port-channel 10, uses MTU 9216, maps to VRF DR-6 and runs MSTP with bridge priority 32768; changes require CAB approval 3 days ahead.

- (F00186) Firewall rule 5566 permits tcp/443 from 10.13.95.0/24 to 10.255.198.0/26 with sampled logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2028-12-15.

- (F00187) Firewall rule 4279 permits tcp/8443 from 10.37.231.0/24 to 10.88.227.0/26 with full logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2029-02-18.

- (F00188) BGP peering between core-3 (AS 65324) and edge-6 (AS 65032) at Brightholm uses timers 3/9s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-MONITORING-1 applies.

- (F00189) BGP peering between core-3 (AS 65138) and edge-2 (AS 64579) at Cresswick uses timers 10/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-BASTION-25 applies.

## Page 22: Load balancing [network]

- (F00190) VLAN 1943 (monitoring-mgmt) is trunked between bri-sw11 and fer-sw03 on port-channel 23, uses MTU 1500, maps to VRF MGMT-3 and runs RSTP with bridge priority 32768; changes require CAB approval 10 days ahead.

- (F00191) VLAN 774 (data-test) is trunked between ald-sw17 and bri-sw10 on port-channel 46, uses MTU 1500, maps to VRF TEST-9 and runs MSTP with bridge priority 4096; changes require CAB approval 6 days ahead.

- (F00192) Firewall rule 5961 permits tcp/9092 from 10.86.78.0/24 to 10.87.172.0/26 with sampled logging; the rule is reviewed every 30 days by Platform Engineering and expires on 2027-01-21.

- (F00193) BGP peering between core-1 (AS 65021) and edge-5 (AS 65169) at Cresswick uses timers 10/9s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-QUEUE-15 applies.

- (F00194) VLAN 1802 (monitoring-dr) is trunked between fer-sw02 and bri-sw15 on port-channel 14, uses MTU 9000, maps to VRF MGMT-3 and runs MSTP with bridge priority 24576; changes require CAB approval 7 days ahead.

- (F00195) Load balancer pool catalogue-test fronts 5 members with round-robin balancing, health probe tcp/443 every 10s and idle timeout 240s; persistence none.

- (F00196) VLAN 1812 (cache-preprod) is trunked between ald-sw10 and dun-sw20 on port-channel 21, uses MTU 9216, maps to VRF TEST-4 and runs RSTP with bridge priority 32768; changes require CAB approval 10 days ahead.

- (F00197) Load balancer pool catalogue-dr fronts 10 members with round-robin balancing, health probe tcp/80 every 30s and idle timeout 300s; persistence none.

- (F00198) VLAN 2854 (monitoring-test) is trunked between cre-sw16 and eas-sw21 on port-channel 35, uses MTU 1500, maps to VRF PROD-7 and runs RSTP with bridge priority 24576; changes require CAB approval 7 days ahead.

## Page 23: Load balancing [network]

- (F00199) BGP peering between core-4 (AS 64883) and edge-5 (AS 64587) at Dunmoor uses timers 30/30s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-APP-5 applies.

- (F00200) VLAN 3945 (batch-preprod) is trunked between dun-sw12 and cre-sw18 on port-channel 13, uses MTU 9216, maps to VRF MGMT-7 and runs RSTP with bridge priority 4096; changes require CAB approval 2 days ahead.

- (F00201) Firewall rule 8487 permits tcp/9092 from 10.71.167.0/24 to 10.163.83.0/26 with drop-only logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2029-09-18.

- (F00202) Load balancer pool ledger-test fronts 7 members with weighted balancing, health probe tcp/443 every 30s and idle timeout 300s; persistence cookie.

- (F00203) VLAN 3306 (cache-prod) is trunked between eas-sw16 and cre-sw21 on port-channel 38, uses MTU 9000, maps to VRF PREPROD-9 and runs MSTP with bridge priority 8192; changes require CAB approval 5 days ahead.

- (F00204) VLAN 177 (monitoring-test) is trunked between eas-sw23 and ald-sw07 on port-channel 27, uses MTU 1500, maps to VRF DR-4 and runs MSTP with bridge priority 32768; changes require CAB approval 2 days ahead.

- (F00205) Firewall rule 8837 permits udp/5432 from 10.88.235.0/24 to 10.175.181.0/26 with sampled logging; the rule is reviewed every 90 days by Service Delivery and expires on 2027-04-09.

- (F00206) BGP peering between core-4 (AS 65218) and edge-8 (AS 64836) at Dunmoor uses timers 10/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-QUEUE-4 applies.

- (F00207) Load balancer pool ledger-test fronts 3 members with round-robin balancing, health probe http/8080 every 10s and idle timeout 900s; persistence none.

## Page 24: Switching fabric [network]

- (F00208) BGP peering between core-2 (AS 65142) and edge-4 (AS 64760) at Aldermere uses timers 30/90s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-CACHE-2 applies.

- (F00209) VLAN 511 (data-prod) is trunked between dun-sw11 and fer-sw16 on port-channel 36, uses MTU 1500, maps to VRF DR-8 and runs MSTP with bridge priority 8192; changes require CAB approval 6 days ahead.

- (F00210) BGP peering between core-4 (AS 65059) and edge-1 (AS 65447) at Brightholm uses timers 10/9s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-MONITORING-6 applies.

- (F00211) BGP peering between core-2 (AS 65462) and edge-6 (AS 64803) at Dunmoor uses timers 30/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-DATA-28 applies.

- (F00212) Load balancer pool scheduler-dr fronts 12 members with round-robin balancing, health probe https/80 every 5s and idle timeout 300s; persistence source-ip.

- (F00213) Firewall rule 8007 permits udp/443 from 10.205.48.0/24 to 10.94.71.0/26 with drop-only logging; the rule is reviewed every 90 days by Network Operations and expires on 2027-05-13.

- (F00214) Firewall rule 1187 permits udp/6379 from 10.184.120.0/24 to 10.31.60.0/26 with drop-only logging; the rule is reviewed every 90 days by Network Operations and expires on 2028-11-17.

- (F00215) BGP peering between core-6 (AS 65141) and edge-4 (AS 64736) at Brightholm uses timers 10/9s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-BATCH-14 applies.

- (F00216) Load balancer pool catalogue-mgmt fronts 9 members with weighted balancing, health probe https/443 every 5s and idle timeout 60s; persistence none.

## Page 25: WAN links [network]

- (F00217) Firewall rule 6375 permits udp/443 from 10.105.250.0/24 to 10.46.228.0/26 with full logging; the rule is reviewed every 180 days by Network Operations and expires on 2029-07-15.

- (F00218) VLAN 3062 (web-dr) is trunked between eas-sw15 and fer-sw10 on port-channel 17, uses MTU 1500, maps to VRF PREPROD-2 and runs RSTP with bridge priority 32768; changes require CAB approval 7 days ahead.

- (F00219) VLAN 229 (queue-dr) is trunked between eas-sw02 and ald-sw16 on port-channel 12, uses MTU 1500, maps to VRF DR-6 and runs MSTP with bridge priority 32768; changes require CAB approval 8 days ahead.

- (F00220) Load balancer pool scheduler-test fronts 3 members with least-connections balancing, health probe https/443 every 30s and idle timeout 240s; persistence cookie.

- (F00221) Firewall rule 9920 permits udp/9092 from 10.194.117.0/24 to 10.126.235.0/26 with drop-only logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2027-12-25.

- (F00222) VLAN 3237 (web-preprod) is trunked between ald-sw22 and dun-sw20 on port-channel 14, uses MTU 1500, maps to VRF PROD-1 and runs MSTP with bridge priority 4096; changes require CAB approval 5 days ahead.

- (F00223) VLAN 989 (web-preprod) is trunked between dun-sw15 and bri-sw18 on port-channel 33, uses MTU 9000, maps to VRF PREPROD-6 and runs MSTP with bridge priority 8192; changes require CAB approval 6 days ahead.

- (F00224) Firewall rule 5923 permits udp/443 from 10.89.218.0/24 to 10.253.24.0/26 with drop-only logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2029-07-14.

- (F00225) Firewall rule 8758 permits tcp/8443 from 10.153.73.0/24 to 10.237.29.0/26 with sampled logging; the rule is reviewed every 180 days by Service Delivery and expires on 2029-09-05.

## Page 26: Load balancing [network]

- (F00226) Firewall rule 2295 permits udp/5432 from 10.47.97.0/24 to 10.26.137.0/26 with drop-only logging; the rule is reviewed every 30 days by Platform Engineering and expires on 2027-10-24.

- (F00227) Firewall rule 1251 permits tcp/8443 from 10.60.245.0/24 to 10.124.104.0/26 with drop-only logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2028-07-15.

- (F00228) BGP peering between core-8 (AS 64989) and edge-2 (AS 65334) at Fernhollow uses timers 10/30s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-BATCH-14 applies.

- (F00229) VLAN 166 (queue-mgmt) is trunked between eas-sw08 and fer-sw05 on port-channel 38, uses MTU 9216, maps to VRF DR-5 and runs RSTP with bridge priority 8192; changes require CAB approval 7 days ahead.

- (F00230) Firewall rule 6530 permits udp/1433 from 10.251.235.0/24 to 10.86.180.0/26 with full logging; the rule is reviewed every 60 days by Service Delivery and expires on 2027-09-21.

- (F00231) VLAN 298 (web-dr) is trunked between eas-sw02 and ald-sw22 on port-channel 9, uses MTU 9216, maps to VRF PREPROD-2 and runs RSTP with bridge priority 4096; changes require CAB approval 5 days ahead.

- (F00232) Load balancer pool identity-dr fronts 2 members with least-connections balancing, health probe https/8080 every 10s and idle timeout 60s; persistence none.

- (F00233) BGP peering between core-7 (AS 65337) and edge-3 (AS 64621) at Aldermere uses timers 30/9s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-QUEUE-27 applies.

- (F00234) BGP peering between core-7 (AS 64982) and edge-4 (AS 65525) at Fernhollow uses timers 3/30s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-WEB-3 applies.

## Page 27: Load balancing [network]

- (F00235) Load balancer pool ledger-preprod fronts 3 members with round-robin balancing, health probe http/8080 every 10s and idle timeout 60s; persistence cookie.

- (F00236) VLAN 2047 (queue-prod) is trunked between bri-sw07 and fer-sw19 on port-channel 5, uses MTU 9216, maps to VRF TEST-9 and runs RSTP with bridge priority 8192; changes require CAB approval 7 days ahead.

- (F00237) VLAN 3462 (bastion-prod) is trunked between bri-sw19 and bri-sw23 on port-channel 20, uses MTU 1500, maps to VRF MGMT-4 and runs MSTP with bridge priority 24576; changes require CAB approval 8 days ahead.

- (F00238) Firewall rule 6666 permits tcp/443 from 10.223.118.0/24 to 10.38.174.0/26 with sampled logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2027-11-09.

- (F00239) Load balancer pool reports-dr fronts 4 members with weighted balancing, health probe https/8080 every 10s and idle timeout 60s; persistence cookie.

- (F00240) BGP peering between core-5 (AS 64669) and edge-7 (AS 65240) at Fernhollow uses timers 3/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-BATCH-4 applies.

- (F00241) VLAN 3218 (queue-prod) is trunked between ald-sw10 and dun-sw12 on port-channel 9, uses MTU 1500, maps to VRF PREPROD-7 and runs MSTP with bridge priority 32768; changes require CAB approval 3 days ahead.

- (F00242) VLAN 2545 (batch-dr) is trunked between ald-sw12 and eas-sw03 on port-channel 1, uses MTU 9000, maps to VRF DR-7 and runs RSTP with bridge priority 8192; changes require CAB approval 10 days ahead.

- (F00243) Firewall rule 5405 permits udp/5432 from 10.252.74.0/24 to 10.32.85.0/26 with drop-only logging; the rule is reviewed every 90 days by Service Delivery and expires on 2028-08-26.

## Page 28: Core routing [network]

- (F00244) BGP peering between core-8 (AS 65120) and edge-4 (AS 64980) at Aldermere uses timers 3/30s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-BATCH-27 applies.

- (F00245) Load balancer pool scheduler-test fronts 7 members with weighted balancing, health probe https/80 every 10s and idle timeout 300s; persistence none.

- (F00246) Load balancer pool identity-mgmt fronts 5 members with round-robin balancing, health probe http/443 every 10s and idle timeout 300s; persistence none.

- (F00247) Firewall rule 1440 permits udp/6379 from 10.107.224.0/24 to 10.149.35.0/26 with drop-only logging; the rule is reviewed every 180 days by Network Operations and expires on 2029-05-08.

- (F00248) BGP peering between core-7 (AS 64587) and edge-8 (AS 65526) at Eastvale uses timers 10/90s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-BASTION-18 applies.

- (F00249) VLAN 2713 (app-prod) is trunked between cre-sw23 and eas-sw20 on port-channel 16, uses MTU 9216, maps to VRF TEST-3 and runs RSTP with bridge priority 32768; changes require CAB approval 7 days ahead.

- (F00250) Load balancer pool gateway-mgmt fronts 10 members with weighted balancing, health probe https/8080 every 30s and idle timeout 240s; persistence source-ip.

- (F00251) BGP peering between core-3 (AS 64865) and edge-1 (AS 65006) at Aldermere uses timers 10/30s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-DATA-12 applies.

- (F00252) BGP peering between core-8 (AS 64868) and edge-8 (AS 64611) at Dunmoor uses timers 30/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-APP-10 applies.

## Page 29: Core routing [network]

- (F00253) VLAN 2873 (data-preprod) is trunked between ald-sw11 and fer-sw04 on port-channel 34, uses MTU 1500, maps to VRF MGMT-3 and runs MSTP with bridge priority 32768; changes require CAB approval 9 days ahead.

- (F00254) Firewall rule 8080 permits udp/443 from 10.101.230.0/24 to 10.219.199.0/26 with full logging; the rule is reviewed every 60 days by Network Operations and expires on 2028-12-26.

- (F00255) VLAN 1598 (batch-preprod) is trunked between eas-sw04 and eas-sw06 on port-channel 30, uses MTU 1500, maps to VRF TEST-8 and runs MSTP with bridge priority 32768; changes require CAB approval 8 days ahead.

- (F00256) VLAN 806 (queue-mgmt) is trunked between cre-sw12 and dun-sw20 on port-channel 38, uses MTU 1500, maps to VRF PREPROD-6 and runs RSTP with bridge priority 8192; changes require CAB approval 6 days ahead.

- (F00257) VLAN 2192 (bastion-dr) is trunked between bri-sw12 and fer-sw05 on port-channel 39, uses MTU 1500, maps to VRF MGMT-7 and runs MSTP with bridge priority 8192; changes require CAB approval 9 days ahead.

- (F00258) Firewall rule 3298 permits tcp/5432 from 10.230.27.0/24 to 10.183.4.0/26 with drop-only logging; the rule is reviewed every 60 days by Network Operations and expires on 2028-09-17.

- (F00259) Load balancer pool identity-dr fronts 4 members with least-connections balancing, health probe https/80 every 5s and idle timeout 300s; persistence none.

- (F00260) BGP peering between core-8 (AS 65091) and edge-8 (AS 65074) at Eastvale uses timers 3/90s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-BATCH-18 applies.

- (F00261) VLAN 1841 (app-preprod) is trunked between fer-sw15 and eas-sw07 on port-channel 20, uses MTU 1500, maps to VRF DR-5 and runs MSTP with bridge priority 4096; changes require CAB approval 9 days ahead.

## Page 30: Core routing [network]

- (F00262) Firewall rule 6744 permits udp/8443 from 10.71.105.0/24 to 10.105.30.0/26 with sampled logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2029-09-06.

- (F00263) BGP peering between core-5 (AS 65487) and edge-2 (AS 64650) at Dunmoor uses timers 3/30s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-DATA-8 applies.

- (F00264) Firewall rule 7434 permits udp/8443 from 10.137.212.0/24 to 10.192.231.0/26 with full logging; the rule is reviewed every 30 days by Service Delivery and expires on 2029-12-09.

- (F00265) BGP peering between core-1 (AS 65401) and edge-2 (AS 65260) at Dunmoor uses timers 30/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-APP-26 applies.

- (F00266) Load balancer pool telemetry-test fronts 6 members with round-robin balancing, health probe https/8080 every 5s and idle timeout 900s; persistence source-ip.

- (F00267) VLAN 166 (app-preprod) is trunked between ald-sw04 and fer-sw15 on port-channel 29, uses MTU 9000, maps to VRF PROD-7 and runs RSTP with bridge priority 8192; changes require CAB approval 6 days ahead.

- (F00268) Firewall rule 5102 permits tcp/5432 from 10.84.26.0/24 to 10.202.156.0/26 with sampled logging; the rule is reviewed every 60 days by Service Delivery and expires on 2029-02-23.

- (F00269) VLAN 643 (cache-mgmt) is trunked between ald-sw07 and dun-sw03 on port-channel 44, uses MTU 9000, maps to VRF PROD-1 and runs MSTP with bridge priority 4096; changes require CAB approval 8 days ahead.

- (F00270) Firewall rule 2463 permits tcp/443 from 10.160.188.0/24 to 10.153.70.0/26 with drop-only logging; the rule is reviewed every 60 days by Network Operations and expires on 2027-09-19.

## Page 31: Core routing [network]

- (F00271) Firewall rule 3480 permits udp/9092 from 10.226.111.0/24 to 10.44.51.0/26 with full logging; the rule is reviewed every 30 days by Service Delivery and expires on 2028-07-11.

- (F00272) Firewall rule 5065 permits udp/6379 from 10.13.154.0/24 to 10.105.96.0/26 with sampled logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2029-01-26.

- (F00273) Firewall rule 9185 permits tcp/9092 from 10.6.184.0/24 to 10.162.67.0/26 with drop-only logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2029-11-06.

- (F00274) Load balancer pool ledger-test fronts 5 members with least-connections balancing, health probe tcp/443 every 30s and idle timeout 300s; persistence cookie.

- (F00275) Load balancer pool scheduler-test fronts 3 members with round-robin balancing, health probe tcp/8080 every 5s and idle timeout 240s; persistence cookie.

- (F00276) BGP peering between core-2 (AS 64829) and edge-7 (AS 65259) at Brightholm uses timers 3/9s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-APP-15 applies.

- (F00277) VLAN 3133 (data-prod) is trunked between cre-sw22 and fer-sw22 on port-channel 1, uses MTU 9216, maps to VRF PREPROD-1 and runs RSTP with bridge priority 32768; changes require CAB approval 7 days ahead.

- (F00278) BGP peering between core-5 (AS 65262) and edge-2 (AS 65301) at Aldermere uses timers 10/30s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-APP-9 applies.

- (F00279) VLAN 327 (monitoring-mgmt) is trunked between dun-sw15 and eas-sw12 on port-channel 11, uses MTU 9000, maps to VRF PREPROD-5 and runs RSTP with bridge priority 4096; changes require CAB approval 5 days ahead.

## Page 32: WAN links [network]

- (F00280) VLAN 2032 (batch-dr) is trunked between ald-sw01 and bri-sw02 on port-channel 10, uses MTU 1500, maps to VRF PROD-9 and runs MSTP with bridge priority 8192; changes require CAB approval 7 days ahead.

- (F00281) Firewall rule 2276 permits udp/443 from 10.26.91.0/24 to 10.114.23.0/26 with drop-only logging; the rule is reviewed every 30 days by Service Delivery and expires on 2028-05-11.

- (F00282) VLAN 921 (queue-mgmt) is trunked between eas-sw15 and ald-sw12 on port-channel 20, uses MTU 9216, maps to VRF MGMT-4 and runs MSTP with bridge priority 24576; changes require CAB approval 9 days ahead.

- (F00283) Firewall rule 1104 permits udp/443 from 10.119.177.0/24 to 10.4.171.0/26 with full logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2027-04-17.

- (F00284) Firewall rule 5584 permits tcp/443 from 10.118.211.0/24 to 10.190.234.0/26 with sampled logging; the rule is reviewed every 30 days by Platform Engineering and expires on 2029-03-21.

- (F00285) Load balancer pool reports-preprod fronts 5 members with round-robin balancing, health probe http/443 every 10s and idle timeout 300s; persistence source-ip.

- (F00286) Load balancer pool scheduler-mgmt fronts 3 members with least-connections balancing, health probe tcp/80 every 10s and idle timeout 900s; persistence source-ip.

- (F00287) Load balancer pool identity-test fronts 9 members with round-robin balancing, health probe tcp/80 every 5s and idle timeout 300s; persistence cookie.

- (F00288) VLAN 3012 (cache-test) is trunked between bri-sw11 and bri-sw03 on port-channel 26, uses MTU 9216, maps to VRF PROD-5 and runs MSTP with bridge priority 8192; changes require CAB approval 2 days ahead.

## Page 33: Load balancing [network]

- (F00289) Load balancer pool catalogue-dr fronts 3 members with least-connections balancing, health probe tcp/80 every 5s and idle timeout 240s; persistence none.

- (F00290) Firewall rule 2376 permits udp/443 from 10.11.33.0/24 to 10.101.227.0/26 with full logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2027-01-15.

- (F00291) VLAN 1717 (monitoring-prod) is trunked between bri-sw19 and dun-sw24 on port-channel 25, uses MTU 9216, maps to VRF DR-3 and runs MSTP with bridge priority 8192; changes require CAB approval 4 days ahead.

- (F00292) BGP peering between core-4 (AS 65174) and edge-5 (AS 65022) at Dunmoor uses timers 30/30s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-QUEUE-13 applies.

- (F00293) Firewall rule 5082 permits tcp/1433 from 10.183.245.0/24 to 10.248.176.0/26 with sampled logging; the rule is reviewed every 90 days by Service Delivery and expires on 2028-03-01.

- (F00294) BGP peering between core-1 (AS 65340) and edge-8 (AS 65054) at Cresswick uses timers 30/9s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-CACHE-22 applies.

- (F00295) Firewall rule 4594 permits udp/5432 from 10.88.90.0/24 to 10.121.162.0/26 with sampled logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2029-12-12.

- (F00296) Firewall rule 6063 permits tcp/1433 from 10.19.46.0/24 to 10.28.119.0/26 with sampled logging; the rule is reviewed every 60 days by Platform Engineering and expires on 2029-08-01.

- (F00297) BGP peering between core-3 (AS 65452) and edge-6 (AS 64572) at Aldermere uses timers 3/90s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-APP-28 applies.

## Page 34: WAN links [network]

- (F00298) BGP peering between core-7 (AS 65112) and edge-2 (AS 64856) at Cresswick uses timers 10/9s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-BASTION-26 applies.

- (F00299) Load balancer pool mailer-preprod fronts 12 members with weighted balancing, health probe tcp/443 every 10s and idle timeout 300s; persistence none.

- (F00300) Firewall rule 7415 permits tcp/8443 from 10.162.113.0/24 to 10.53.254.0/26 with full logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2027-06-11.

- (F00301) Firewall rule 6500 permits udp/443 from 10.135.107.0/24 to 10.127.34.0/26 with drop-only logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2029-01-02.

- (F00302) Load balancer pool reports-dr fronts 8 members with round-robin balancing, health probe https/443 every 5s and idle timeout 900s; persistence cookie.

- (F00303) Firewall rule 5831 permits tcp/5432 from 10.133.53.0/24 to 10.37.175.0/26 with full logging; the rule is reviewed every 180 days by Network Operations and expires on 2029-02-18.

- (F00304) VLAN 2985 (web-dr) is trunked between cre-sw20 and eas-sw16 on port-channel 42, uses MTU 1500, maps to VRF MGMT-7 and runs RSTP with bridge priority 4096; changes require CAB approval 3 days ahead.

- (F00305) BGP peering between core-5 (AS 65188) and edge-5 (AS 64816) at Brightholm uses timers 3/9s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-MONITORING-5 applies.

- (F00306) VLAN 1306 (monitoring-preprod) is trunked between cre-sw01 and dun-sw03 on port-channel 7, uses MTU 1500, maps to VRF PREPROD-3 and runs MSTP with bridge priority 4096; changes require CAB approval 9 days ahead.

## Page 35: Core routing [network]

- (F00307) BGP peering between core-5 (AS 64605) and edge-7 (AS 64701) at Cresswick uses timers 10/30s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-WEB-9 applies.

- (F00308) Load balancer pool ledger-preprod fronts 12 members with least-connections balancing, health probe tcp/8080 every 10s and idle timeout 900s; persistence cookie.

- (F00309) Firewall rule 7858 permits udp/9092 from 10.120.243.0/24 to 10.153.40.0/26 with drop-only logging; the rule is reviewed every 30 days by Network Operations and expires on 2027-08-06.

- (F00310) Firewall rule 7936 permits tcp/6379 from 10.222.103.0/24 to 10.75.132.0/26 with drop-only logging; the rule is reviewed every 30 days by Platform Engineering and expires on 2028-09-13.

- (F00311) BGP peering between core-7 (AS 64627) and edge-7 (AS 64665) at Brightholm uses timers 30/90s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-APP-19 applies.

- (F00312) VLAN 1181 (bastion-dr) is trunked between cre-sw18 and cre-sw14 on port-channel 37, uses MTU 9216, maps to VRF DR-1 and runs RSTP with bridge priority 24576; changes require CAB approval 8 days ahead.

- (F00313) Firewall rule 7581 permits tcp/1433 from 10.169.121.0/24 to 10.25.243.0/26 with drop-only logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2028-05-10.

- (F00314) BGP peering between core-4 (AS 64649) and edge-5 (AS 65509) at Fernhollow uses timers 10/30s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-BASTION-20 applies.

- (F00315) VLAN 3134 (monitoring-mgmt) is trunked between bri-sw15 and bri-sw14 on port-channel 24, uses MTU 1500, maps to VRF MGMT-3 and runs RSTP with bridge priority 24576; changes require CAB approval 10 days ahead.

## Page 36: Load balancing [network]

- (F00316) Firewall rule 4158 permits tcp/443 from 10.127.16.0/24 to 10.233.25.0/26 with drop-only logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2028-08-17.

- (F00317) Load balancer pool gateway-test fronts 9 members with weighted balancing, health probe http/80 every 10s and idle timeout 300s; persistence source-ip.

- (F00318) Firewall rule 5670 permits tcp/1433 from 10.25.83.0/24 to 10.109.113.0/26 with sampled logging; the rule is reviewed every 60 days by Network Operations and expires on 2028-11-14.

- (F00319) VLAN 2751 (data-mgmt) is trunked between fer-sw01 and dun-sw05 on port-channel 1, uses MTU 1500, maps to VRF TEST-5 and runs MSTP with bridge priority 32768; changes require CAB approval 8 days ahead.

- (F00320) BGP peering between core-5 (AS 65205) and edge-7 (AS 65110) at Aldermere uses timers 3/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-QUEUE-10 applies.

- (F00321) VLAN 2723 (batch-test) is trunked between dun-sw03 and cre-sw09 on port-channel 17, uses MTU 9216, maps to VRF TEST-4 and runs RSTP with bridge priority 8192; changes require CAB approval 2 days ahead.

- (F00322) Load balancer pool ledger-dr fronts 6 members with round-robin balancing, health probe http/443 every 10s and idle timeout 60s; persistence cookie.

- (F00323) Firewall rule 9759 permits udp/6379 from 10.183.153.0/24 to 10.87.92.0/26 with drop-only logging; the rule is reviewed every 30 days by Service Delivery and expires on 2027-12-09.

- (F00324) Firewall rule 4641 permits udp/8443 from 10.157.215.0/24 to 10.169.190.0/26 with drop-only logging; the rule is reviewed every 90 days by Service Delivery and expires on 2027-08-02.

## Page 37: WAN links [network]

- (F00325) VLAN 3653 (bastion-mgmt) is trunked between dun-sw07 and eas-sw04 on port-channel 20, uses MTU 9000, maps to VRF PROD-3 and runs RSTP with bridge priority 8192; changes require CAB approval 7 days ahead.

- (F00326) Load balancer pool scheduler-prod fronts 9 members with round-robin balancing, health probe https/80 every 10s and idle timeout 60s; persistence none.

- (F00327) Load balancer pool scheduler-dr fronts 3 members with least-connections balancing, health probe https/443 every 30s and idle timeout 900s; persistence source-ip.

- (F00328) Load balancer pool gateway-test fronts 2 members with round-robin balancing, health probe https/80 every 5s and idle timeout 60s; persistence cookie.

- (F00329) Firewall rule 3112 permits tcp/1433 from 10.156.85.0/24 to 10.33.23.0/26 with drop-only logging; the rule is reviewed every 90 days by Service Delivery and expires on 2029-09-20.

- (F00330) BGP peering between core-8 (AS 64879) and edge-4 (AS 64680) at Dunmoor uses timers 3/9s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-DATA-7 applies.

- (F00331) VLAN 1601 (web-dr) is trunked between eas-sw17 and bri-sw04 on port-channel 41, uses MTU 9000, maps to VRF MGMT-1 and runs RSTP with bridge priority 4096; changes require CAB approval 2 days ahead.

- (F00332) VLAN 1657 (app-mgmt) is trunked between fer-sw04 and dun-sw15 on port-channel 17, uses MTU 9000, maps to VRF PREPROD-4 and runs RSTP with bridge priority 24576; changes require CAB approval 8 days ahead.

- (F00333) VLAN 2580 (data-dr) is trunked between fer-sw17 and cre-sw20 on port-channel 7, uses MTU 9216, maps to VRF MGMT-2 and runs MSTP with bridge priority 4096; changes require CAB approval 3 days ahead.

## Page 38: Load balancing [network]

- (F00334) Firewall rule 4304 permits udp/6379 from 10.209.151.0/24 to 10.82.20.0/26 with sampled logging; the rule is reviewed every 180 days by Network Operations and expires on 2029-08-11.

- (F00335) Firewall rule 2809 permits udp/8443 from 10.46.38.0/24 to 10.51.131.0/26 with sampled logging; the rule is reviewed every 60 days by Service Delivery and expires on 2028-05-15.

- (F00336) VLAN 1575 (batch-dr) is trunked between ald-sw06 and ald-sw10 on port-channel 48, uses MTU 1500, maps to VRF PROD-1 and runs RSTP with bridge priority 8192; changes require CAB approval 4 days ahead.

- (F00337) BGP peering between core-2 (AS 64893) and edge-6 (AS 64699) at Aldermere uses timers 10/30s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-BASTION-23 applies.

- (F00338) Load balancer pool scheduler-prod fronts 4 members with least-connections balancing, health probe http/8080 every 10s and idle timeout 900s; persistence none.

- (F00339) Load balancer pool scheduler-dr fronts 9 members with least-connections balancing, health probe http/443 every 5s and idle timeout 60s; persistence source-ip.

- (F00340) BGP peering between core-4 (AS 65513) and edge-6 (AS 65043) at Eastvale uses timers 30/90s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-BASTION-22 applies.

- (F00341) Firewall rule 7305 permits tcp/9092 from 10.27.5.0/24 to 10.80.240.0/26 with drop-only logging; the rule is reviewed every 60 days by Platform Engineering and expires on 2028-06-08.

- (F00342) BGP peering between core-7 (AS 64924) and edge-4 (AS 64592) at Dunmoor uses timers 10/90s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-MONITORING-15 applies.

## Page 39: Perimeter firewalls [network]

- (F00343) VLAN 520 (bastion-dr) is trunked between dun-sw24 and fer-sw01 on port-channel 3, uses MTU 9216, maps to VRF MGMT-1 and runs RSTP with bridge priority 24576; changes require CAB approval 10 days ahead.

- (F00344) Firewall rule 6953 permits tcp/8443 from 10.232.169.0/24 to 10.242.186.0/26 with sampled logging; the rule is reviewed every 180 days by Platform Engineering and expires on 2027-11-08.

- (F00345) VLAN 2343 (batch-prod) is trunked between cre-sw12 and fer-sw10 on port-channel 3, uses MTU 1500, maps to VRF DR-3 and runs MSTP with bridge priority 4096; changes require CAB approval 6 days ahead.

- (F00346) Firewall rule 8488 permits tcp/6379 from 10.173.55.0/24 to 10.212.23.0/26 with sampled logging; the rule is reviewed every 30 days by Service Delivery and expires on 2028-11-19.

- (F00347) Firewall rule 1795 permits udp/9092 from 10.247.90.0/24 to 10.88.65.0/26 with full logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2029-07-14.

- (F00348) Firewall rule 8419 permits tcp/8443 from 10.211.153.0/24 to 10.160.111.0/26 with full logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2029-06-22.

- (F00349) Firewall rule 9888 permits udp/6379 from 10.59.180.0/24 to 10.245.213.0/26 with sampled logging; the rule is reviewed every 90 days by Service Delivery and expires on 2027-09-04.

- (F00350) VLAN 331 (cache-test) is trunked between dun-sw05 and ald-sw22 on port-channel 11, uses MTU 9000, maps to VRF TEST-3 and runs RSTP with bridge priority 24576; changes require CAB approval 5 days ahead.

- (F00351) VLAN 3655 (cache-mgmt) is trunked between cre-sw15 and ald-sw20 on port-channel 25, uses MTU 1500, maps to VRF MGMT-5 and runs RSTP with bridge priority 32768; changes require CAB approval 8 days ahead.

## Page 40: Load balancing [network]

- (F00352) BGP peering between core-5 (AS 64719) and edge-8 (AS 65361) at Brightholm uses timers 30/90s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-BATCH-25 applies.

- (F00353) Firewall rule 3906 permits tcp/8443 from 10.88.61.0/24 to 10.193.20.0/26 with drop-only logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2027-03-19.

- (F00354) BGP peering between core-3 (AS 64552) and edge-3 (AS 65462) at Cresswick uses timers 30/9s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-QUEUE-16 applies.

- (F00355) BGP peering between core-4 (AS 65491) and edge-3 (AS 65045) at Aldermere uses timers 30/9s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-BASTION-3 applies.

- (F00356) BGP peering between core-6 (AS 64881) and edge-5 (AS 64735) at Eastvale uses timers 30/30s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-WEB-4 applies.

- (F00357) BGP peering between core-4 (AS 65493) and edge-1 (AS 65210) at Cresswick uses timers 10/9s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-QUEUE-1 applies.

- (F00358) BGP peering between core-1 (AS 64815) and edge-4 (AS 64840) at Eastvale uses timers 3/9s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-WEB-21 applies.

- (F00359) VLAN 3642 (bastion-prod) is trunked between bri-sw22 and fer-sw07 on port-channel 14, uses MTU 9216, maps to VRF DR-2 and runs RSTP with bridge priority 4096; changes require CAB approval 9 days ahead.

- (F00360) BGP peering between core-3 (AS 65325) and edge-5 (AS 65083) at Aldermere uses timers 30/9s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-BASTION-15 applies.

## Page 41: Load balancing [network]

- (F00361) Load balancer pool catalogue-mgmt fronts 2 members with weighted balancing, health probe https/8080 every 5s and idle timeout 60s; persistence cookie.

- (F00362) VLAN 3323 (queue-mgmt) is trunked between cre-sw17 and ald-sw10 on port-channel 6, uses MTU 9000, maps to VRF DR-7 and runs MSTP with bridge priority 4096; changes require CAB approval 9 days ahead.

- (F00363) Firewall rule 7406 permits udp/6379 from 10.73.152.0/24 to 10.191.5.0/26 with sampled logging; the rule is reviewed every 60 days by Platform Engineering and expires on 2027-01-19.

- (F00364) Load balancer pool gateway-test fronts 5 members with round-robin balancing, health probe https/8080 every 5s and idle timeout 240s; persistence none.

- (F00365) Firewall rule 3971 permits tcp/9092 from 10.236.37.0/24 to 10.148.34.0/26 with drop-only logging; the rule is reviewed every 30 days by Network Operations and expires on 2029-10-16.

- (F00366) BGP peering between core-4 (AS 64614) and edge-5 (AS 65146) at Aldermere uses timers 3/30s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-BATCH-20 applies.

- (F00367) BGP peering between core-6 (AS 65339) and edge-6 (AS 65493) at Dunmoor uses timers 3/9s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-CACHE-23 applies.

- (F00368) Load balancer pool mailer-dr fronts 9 members with round-robin balancing, health probe http/443 every 10s and idle timeout 60s; persistence none.

- (F00369) VLAN 1178 (app-prod) is trunked between cre-sw05 and eas-sw07 on port-channel 2, uses MTU 9216, maps to VRF PROD-7 and runs RSTP with bridge priority 4096; changes require CAB approval 10 days ahead.

## Page 42: Perimeter firewalls [network]

- (F00370) Load balancer pool gateway-mgmt fronts 6 members with least-connections balancing, health probe http/8080 every 30s and idle timeout 60s; persistence source-ip.

- (F00371) BGP peering between core-3 (AS 65287) and edge-3 (AS 64968) at Brightholm uses timers 3/90s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-DATA-24 applies.

- (F00372) Load balancer pool gateway-prod fronts 6 members with round-robin balancing, health probe tcp/80 every 30s and idle timeout 240s; persistence cookie.

- (F00373) BGP peering between core-1 (AS 65516) and edge-6 (AS 64617) at Fernhollow uses timers 30/90s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-QUEUE-19 applies.

- (F00374) Firewall rule 2275 permits udp/1433 from 10.114.207.0/24 to 10.180.176.0/26 with drop-only logging; the rule is reviewed every 180 days by Platform Engineering and expires on 2029-03-15.

- (F00375) Firewall rule 5600 permits tcp/8443 from 10.95.80.0/24 to 10.185.60.0/26 with sampled logging; the rule is reviewed every 60 days by Service Delivery and expires on 2028-12-04.

- (F00376) Load balancer pool scheduler-dr fronts 2 members with least-connections balancing, health probe tcp/80 every 30s and idle timeout 240s; persistence none.

- (F00377) VLAN 1157 (data-mgmt) is trunked between eas-sw05 and ald-sw06 on port-channel 26, uses MTU 9216, maps to VRF MGMT-1 and runs MSTP with bridge priority 4096; changes require CAB approval 5 days ahead.

- (F00378) Load balancer pool gateway-dr fronts 11 members with least-connections balancing, health probe https/80 every 30s and idle timeout 300s; persistence none.

## Page 43: Perimeter firewalls [network]

- (F00379) Load balancer pool reports-dr fronts 4 members with least-connections balancing, health probe tcp/80 every 30s and idle timeout 900s; persistence none.

- (F00380) VLAN 259 (app-prod) is trunked between bri-sw16 and eas-sw20 on port-channel 31, uses MTU 9216, maps to VRF PREPROD-9 and runs RSTP with bridge priority 32768; changes require CAB approval 10 days ahead.

- (F00381) Load balancer pool reports-preprod fronts 9 members with round-robin balancing, health probe http/8080 every 30s and idle timeout 60s; persistence source-ip.

- (F00382) Firewall rule 5641 permits udp/5432 from 10.96.2.0/24 to 10.3.60.0/26 with sampled logging; the rule is reviewed every 30 days by Service Delivery and expires on 2029-04-23.

- (F00383) BGP peering between core-7 (AS 65179) and edge-5 (AS 64779) at Eastvale uses timers 10/90s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-QUEUE-22 applies.

- (F00384) Load balancer pool identity-preprod fronts 7 members with weighted balancing, health probe https/443 every 10s and idle timeout 300s; persistence cookie.

- (F00385) BGP peering between core-2 (AS 65277) and edge-4 (AS 64969) at Fernhollow uses timers 3/9s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-BASTION-26 applies.

- (F00386) BGP peering between core-1 (AS 64676) and edge-7 (AS 65499) at Fernhollow uses timers 3/9s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-BASTION-3 applies.

- (F00387) VLAN 2594 (web-dr) is trunked between cre-sw08 and cre-sw03 on port-channel 26, uses MTU 9216, maps to VRF MGMT-5 and runs RSTP with bridge priority 8192; changes require CAB approval 9 days ahead.

## Page 44: Load balancing [network]

- (F00388) VLAN 897 (web-mgmt) is trunked between bri-sw22 and eas-sw10 on port-channel 33, uses MTU 9216, maps to VRF PREPROD-3 and runs RSTP with bridge priority 24576; changes require CAB approval 5 days ahead.

- (F00389) VLAN 1546 (bastion-dr) is trunked between bri-sw03 and cre-sw13 on port-channel 38, uses MTU 1500, maps to VRF MGMT-1 and runs RSTP with bridge priority 4096; changes require CAB approval 10 days ahead.

- (F00390) BGP peering between core-6 (AS 65498) and edge-5 (AS 64743) at Eastvale uses timers 3/30s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-WEB-9 applies.

- (F00391) Firewall rule 2185 permits udp/5432 from 10.59.131.0/24 to 10.128.226.0/26 with drop-only logging; the rule is reviewed every 180 days by Network Operations and expires on 2028-08-22.

- (F00392) Load balancer pool telemetry-prod fronts 8 members with weighted balancing, health probe tcp/8080 every 30s and idle timeout 240s; persistence source-ip.

- (F00393) Load balancer pool telemetry-preprod fronts 6 members with least-connections balancing, health probe http/8080 every 30s and idle timeout 300s; persistence none.

- (F00394) Firewall rule 5408 permits tcp/6379 from 10.97.255.0/24 to 10.102.120.0/26 with sampled logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2027-04-07.

- (F00395) Firewall rule 2964 permits tcp/6379 from 10.252.3.0/24 to 10.21.246.0/26 with drop-only logging; the rule is reviewed every 90 days by Service Delivery and expires on 2029-05-16.

- (F00396) Firewall rule 3101 permits tcp/9092 from 10.216.244.0/24 to 10.16.177.0/26 with drop-only logging; the rule is reviewed every 60 days by Service Delivery and expires on 2027-12-17.

## Page 45: Load balancing [network]

- (F00397) BGP peering between core-4 (AS 64900) and edge-2 (AS 64845) at Cresswick uses timers 30/30s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-QUEUE-8 applies.

- (F00398) BGP peering between core-3 (AS 65022) and edge-7 (AS 64727) at Dunmoor uses timers 30/30s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-QUEUE-15 applies.

- (F00399) Firewall rule 4744 permits tcp/6379 from 10.138.120.0/24 to 10.221.195.0/26 with full logging; the rule is reviewed every 60 days by Network Operations and expires on 2028-01-06.

- (F00400) Load balancer pool mailer-dr fronts 6 members with round-robin balancing, health probe https/8080 every 5s and idle timeout 900s; persistence none.

- (F00401) Firewall rule 2577 permits udp/6379 from 10.171.133.0/24 to 10.184.184.0/26 with sampled logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2027-07-04.

- (F00402) BGP peering between core-3 (AS 65514) and edge-5 (AS 64875) at Cresswick uses timers 30/90s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-MONITORING-29 applies.

- (F00403) VLAN 2687 (data-preprod) is trunked between dun-sw20 and cre-sw15 on port-channel 41, uses MTU 9000, maps to VRF DR-7 and runs RSTP with bridge priority 4096; changes require CAB approval 4 days ahead.

- (F00404) BGP peering between core-5 (AS 65239) and edge-5 (AS 65131) at Fernhollow uses timers 10/30s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-MONITORING-14 applies.

- (F00405) Firewall rule 4844 permits udp/6379 from 10.40.107.0/24 to 10.85.203.0/26 with full logging; the rule is reviewed every 30 days by Platform Engineering and expires on 2028-09-02.

## Page 46: Core routing [network]

- (F00406) Load balancer pool scheduler-prod fronts 12 members with round-robin balancing, health probe http/80 every 5s and idle timeout 300s; persistence source-ip.

- (F00407) Firewall rule 1575 permits udp/5432 from 10.243.239.0/24 to 10.139.227.0/26 with full logging; the rule is reviewed every 60 days by Service Delivery and expires on 2029-12-21.

- (F00408) Load balancer pool telemetry-test fronts 9 members with weighted balancing, health probe tcp/80 every 10s and idle timeout 300s; persistence source-ip.

- (F00409) Load balancer pool ledger-mgmt fronts 4 members with round-robin balancing, health probe http/443 every 30s and idle timeout 60s; persistence cookie.

- (F00410) Load balancer pool telemetry-mgmt fronts 5 members with least-connections balancing, health probe https/443 every 5s and idle timeout 900s; persistence cookie.

- (F00411) Load balancer pool reports-dr fronts 5 members with round-robin balancing, health probe tcp/443 every 30s and idle timeout 240s; persistence cookie.

- (F00412) BGP peering between core-5 (AS 64934) and edge-4 (AS 65385) at Aldermere uses timers 3/9s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-MONITORING-20 applies.

- (F00413) Load balancer pool gateway-test fronts 2 members with least-connections balancing, health probe tcp/8080 every 5s and idle timeout 240s; persistence none.

- (F00414) BGP peering between core-1 (AS 64750) and edge-2 (AS 64666) at Aldermere uses timers 10/9s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-QUEUE-26 applies.

## Page 47: Load balancing [network]

- (F00415) BGP peering between core-2 (AS 65375) and edge-3 (AS 64569) at Cresswick uses timers 10/9s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-DATA-7 applies.

- (F00416) BGP peering between core-4 (AS 64906) and edge-8 (AS 64765) at Fernhollow uses timers 3/9s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-APP-17 applies.

- (F00417) Firewall rule 6293 permits tcp/6379 from 10.21.62.0/24 to 10.129.246.0/26 with sampled logging; the rule is reviewed every 90 days by Network Operations and expires on 2028-01-28.

- (F00418) Firewall rule 6316 permits tcp/8443 from 10.141.61.0/24 to 10.202.124.0/26 with full logging; the rule is reviewed every 30 days by Service Delivery and expires on 2029-10-05.

- (F00419) BGP peering between core-2 (AS 65214) and edge-6 (AS 65465) at Fernhollow uses timers 3/9s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-DATA-23 applies.

- (F00420) VLAN 2387 (batch-dr) is trunked between bri-sw16 and bri-sw11 on port-channel 47, uses MTU 1500, maps to VRF PROD-7 and runs MSTP with bridge priority 8192; changes require CAB approval 6 days ahead.

- (F00421) VLAN 1307 (monitoring-preprod) is trunked between dun-sw23 and dun-sw18 on port-channel 37, uses MTU 1500, maps to VRF MGMT-6 and runs MSTP with bridge priority 32768; changes require CAB approval 6 days ahead.

- (F00422) Firewall rule 5844 permits udp/9092 from 10.187.232.0/24 to 10.0.194.0/26 with sampled logging; the rule is reviewed every 60 days by Platform Engineering and expires on 2029-06-25.

- (F00423) Firewall rule 9830 permits udp/8443 from 10.254.78.0/24 to 10.144.165.0/26 with drop-only logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2027-09-22.

## Page 48: Core routing [network]

- (F00424) VLAN 538 (monitoring-preprod) is trunked between bri-sw06 and ald-sw07 on port-channel 7, uses MTU 1500, maps to VRF MGMT-7 and runs MSTP with bridge priority 24576; changes require CAB approval 2 days ahead.

- (F00425) BGP peering between core-1 (AS 65464) and edge-4 (AS 65183) at Dunmoor uses timers 3/30s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-BATCH-18 applies.

- (F00426) Load balancer pool telemetry-mgmt fronts 2 members with weighted balancing, health probe tcp/443 every 5s and idle timeout 240s; persistence cookie.

- (F00427) VLAN 1678 (cache-preprod) is trunked between ald-sw24 and bri-sw18 on port-channel 34, uses MTU 9216, maps to VRF PREPROD-3 and runs MSTP with bridge priority 4096; changes require CAB approval 7 days ahead.

- (F00428) Load balancer pool scheduler-preprod fronts 10 members with round-robin balancing, health probe https/443 every 30s and idle timeout 240s; persistence cookie.

- (F00429) Load balancer pool mailer-dr fronts 12 members with round-robin balancing, health probe https/443 every 30s and idle timeout 240s; persistence cookie.

- (F00430) Firewall rule 6898 permits udp/1433 from 10.203.0.0/24 to 10.17.145.0/26 with sampled logging; the rule is reviewed every 30 days by Network Operations and expires on 2028-01-10.

- (F00431) Firewall rule 5521 permits tcp/443 from 10.19.235.0/24 to 10.182.79.0/26 with full logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2029-04-08.

- (F00432) BGP peering between core-4 (AS 65263) and edge-2 (AS 65252) at Cresswick uses timers 10/9s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-APP-20 applies.

## Page 49: Perimeter firewalls [network]

- (F00433) VLAN 3295 (web-test) is trunked between fer-sw19 and dun-sw03 on port-channel 23, uses MTU 9000, maps to VRF DR-2 and runs RSTP with bridge priority 4096; changes require CAB approval 8 days ahead.

- (F00434) VLAN 2311 (data-test) is trunked between cre-sw17 and ald-sw11 on port-channel 33, uses MTU 9216, maps to VRF PREPROD-3 and runs RSTP with bridge priority 32768; changes require CAB approval 9 days ahead.

- (F00435) VLAN 706 (data-test) is trunked between bri-sw14 and cre-sw13 on port-channel 6, uses MTU 9000, maps to VRF MGMT-1 and runs MSTP with bridge priority 24576; changes require CAB approval 3 days ahead.

- (F00436) Load balancer pool scheduler-dr fronts 10 members with least-connections balancing, health probe http/443 every 30s and idle timeout 240s; persistence cookie.

- (F00437) Firewall rule 6298 permits tcp/443 from 10.211.216.0/24 to 10.187.178.0/26 with full logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2029-11-01.

- (F00438) BGP peering between core-3 (AS 64963) and edge-1 (AS 65458) at Brightholm uses timers 3/90s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-APP-4 applies.

- (F00439) VLAN 156 (batch-prod) is trunked between bri-sw20 and bri-sw10 on port-channel 20, uses MTU 9000, maps to VRF DR-1 and runs MSTP with bridge priority 8192; changes require CAB approval 10 days ahead.

- (F00440) Firewall rule 9991 permits udp/9092 from 10.72.9.0/24 to 10.192.22.0/26 with drop-only logging; the rule is reviewed every 60 days by Platform Engineering and expires on 2028-04-26.

- (F00441) BGP peering between core-2 (AS 64909) and edge-5 (AS 65190) at Fernhollow uses timers 10/9s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-BASTION-8 applies.

## Page 50: Load balancing [network]

- (F00442) VLAN 460 (data-preprod) is trunked between cre-sw16 and eas-sw18 on port-channel 33, uses MTU 9000, maps to VRF MGMT-1 and runs RSTP with bridge priority 8192; changes require CAB approval 10 days ahead.

- (F00443) BGP peering between core-3 (AS 64530) and edge-6 (AS 65212) at Cresswick uses timers 10/90s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-QUEUE-26 applies.

- (F00444) VLAN 3967 (queue-preprod) is trunked between fer-sw09 and dun-sw01 on port-channel 10, uses MTU 9000, maps to VRF DR-3 and runs RSTP with bridge priority 32768; changes require CAB approval 10 days ahead.

- (F00445) Firewall rule 7987 permits udp/9092 from 10.168.229.0/24 to 10.67.105.0/26 with sampled logging; the rule is reviewed every 60 days by Network Operations and expires on 2027-05-23.

- (F00446) Firewall rule 3589 permits udp/443 from 10.60.94.0/24 to 10.162.74.0/26 with sampled logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2028-07-10.

- (F00447) Load balancer pool scheduler-preprod fronts 3 members with least-connections balancing, health probe tcp/80 every 30s and idle timeout 300s; persistence cookie.

- (F00448) Firewall rule 1427 permits udp/443 from 10.244.68.0/24 to 10.240.191.0/26 with full logging; the rule is reviewed every 180 days by Service Delivery and expires on 2028-03-06.

- (F00449) Firewall rule 5421 permits udp/8443 from 10.103.104.0/24 to 10.33.90.0/26 with drop-only logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2028-04-14.

- (F00450) Load balancer pool mailer-dr fronts 11 members with weighted balancing, health probe https/8080 every 30s and idle timeout 60s; persistence cookie.

## Page 51: Core routing [network]

- (F00451) Load balancer pool reports-prod fronts 10 members with round-robin balancing, health probe https/8080 every 5s and idle timeout 240s; persistence source-ip.

- (F00452) Load balancer pool scheduler-dr fronts 6 members with weighted balancing, health probe tcp/8080 every 30s and idle timeout 240s; persistence source-ip.

- (F00453) Load balancer pool scheduler-mgmt fronts 10 members with least-connections balancing, health probe http/443 every 10s and idle timeout 900s; persistence none.

- (F00454) Firewall rule 8449 permits tcp/5432 from 10.165.83.0/24 to 10.63.46.0/26 with full logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2027-09-23.

- (F00455) Load balancer pool reports-mgmt fronts 8 members with least-connections balancing, health probe tcp/443 every 30s and idle timeout 240s; persistence none.

- (F00456) Firewall rule 6047 permits udp/6379 from 10.228.147.0/24 to 10.92.60.0/26 with full logging; the rule is reviewed every 60 days by Platform Engineering and expires on 2029-05-01.

- (F00457) Load balancer pool identity-preprod fronts 5 members with weighted balancing, health probe https/443 every 10s and idle timeout 900s; persistence source-ip.

- (F00458) VLAN 3713 (queue-mgmt) is trunked between eas-sw20 and ald-sw08 on port-channel 41, uses MTU 9216, maps to VRF PREPROD-1 and runs RSTP with bridge priority 8192; changes require CAB approval 2 days ahead.

- (F00459) BGP peering between core-5 (AS 64851) and edge-2 (AS 64562) at Aldermere uses timers 10/9s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-QUEUE-20 applies.

## Page 52: WAN links [network]

- (F00460) Firewall rule 1587 permits tcp/5432 from 10.165.188.0/24 to 10.194.34.0/26 with drop-only logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2028-03-04.

- (F00461) BGP peering between core-4 (AS 65224) and edge-4 (AS 65138) at Aldermere uses timers 3/90s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-APP-16 applies.

- (F00462) BGP peering between core-6 (AS 65461) and edge-3 (AS 65141) at Eastvale uses timers 10/90s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-MONITORING-16 applies.

- (F00463) Firewall rule 4171 permits tcp/443 from 10.12.238.0/24 to 10.60.106.0/26 with sampled logging; the rule is reviewed every 180 days by Service Delivery and expires on 2027-06-12.

- (F00464) Firewall rule 5614 permits udp/443 from 10.157.153.0/24 to 10.165.3.0/26 with full logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2028-12-19.

- (F00465) VLAN 3877 (monitoring-dr) is trunked between bri-sw07 and cre-sw11 on port-channel 3, uses MTU 9216, maps to VRF PREPROD-8 and runs RSTP with bridge priority 32768; changes require CAB approval 10 days ahead.

- (F00466) BGP peering between core-5 (AS 65090) and edge-6 (AS 65080) at Eastvale uses timers 3/9s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-BATCH-26 applies.

- (F00467) BGP peering between core-6 (AS 65519) and edge-7 (AS 65153) at Eastvale uses timers 3/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-DATA-20 applies.

- (F00468) VLAN 229 (queue-dr) is trunked between cre-sw23 and cre-sw23 on port-channel 6, uses MTU 9000, maps to VRF PREPROD-6 and runs MSTP with bridge priority 24576; changes require CAB approval 5 days ahead.

## Page 53: WAN links [network]

- (F00469) BGP peering between core-4 (AS 65447) and edge-2 (AS 64966) at Eastvale uses timers 3/30s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-CACHE-11 applies.

- (F00470) Load balancer pool scheduler-prod fronts 10 members with weighted balancing, health probe tcp/80 every 30s and idle timeout 60s; persistence source-ip.

- (F00471) Load balancer pool telemetry-prod fronts 12 members with weighted balancing, health probe tcp/443 every 10s and idle timeout 60s; persistence none.

- (F00472) BGP peering between core-4 (AS 64840) and edge-4 (AS 64709) at Cresswick uses timers 10/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-APP-9 applies.

- (F00473) Firewall rule 9422 permits tcp/8443 from 10.179.163.0/24 to 10.138.72.0/26 with sampled logging; the rule is reviewed every 90 days by Network Operations and expires on 2027-02-10.

- (F00474) BGP peering between core-1 (AS 64994) and edge-1 (AS 64620) at Dunmoor uses timers 3/9s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-DATA-23 applies.

- (F00475) Load balancer pool gateway-mgmt fronts 3 members with round-robin balancing, health probe https/80 every 5s and idle timeout 900s; persistence none.

- (F00476) Load balancer pool identity-dr fronts 5 members with least-connections balancing, health probe tcp/8080 every 10s and idle timeout 300s; persistence source-ip.

- (F00477) Firewall rule 8426 permits udp/443 from 10.33.243.0/24 to 10.57.179.0/26 with drop-only logging; the rule is reviewed every 180 days by Network Operations and expires on 2028-06-20.

## Page 54: WAN links [network]

- (F00478) Firewall rule 2752 permits udp/9092 from 10.36.154.0/24 to 10.236.205.0/26 with sampled logging; the rule is reviewed every 180 days by Network Operations and expires on 2029-04-18.

- (F00479) Firewall rule 4411 permits udp/1433 from 10.175.120.0/24 to 10.88.39.0/26 with sampled logging; the rule is reviewed every 180 days by Platform Engineering and expires on 2029-10-15.

- (F00480) BGP peering between core-5 (AS 65490) and edge-7 (AS 64583) at Eastvale uses timers 3/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-BATCH-16 applies.

- (F00481) VLAN 3799 (web-preprod) is trunked between ald-sw07 and bri-sw19 on port-channel 43, uses MTU 1500, maps to VRF DR-9 and runs MSTP with bridge priority 32768; changes require CAB approval 9 days ahead.

- (F00482) Firewall rule 5989 permits udp/6379 from 10.176.45.0/24 to 10.4.206.0/26 with full logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2028-09-02.

- (F00483) VLAN 3627 (queue-prod) is trunked between fer-sw18 and cre-sw04 on port-channel 16, uses MTU 9000, maps to VRF MGMT-7 and runs MSTP with bridge priority 32768; changes require CAB approval 8 days ahead.

- (F00484) Load balancer pool scheduler-dr fronts 4 members with least-connections balancing, health probe https/443 every 10s and idle timeout 900s; persistence none.

- (F00485) BGP peering between core-2 (AS 65175) and edge-1 (AS 64659) at Fernhollow uses timers 10/90s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-APP-5 applies.

- (F00486) Load balancer pool scheduler-dr fronts 10 members with round-robin balancing, health probe https/443 every 10s and idle timeout 300s; persistence none.

## Page 55: Switching fabric [network]

- (F00487) Load balancer pool gateway-mgmt fronts 6 members with round-robin balancing, health probe https/8080 every 10s and idle timeout 60s; persistence none.

- (F00488) Load balancer pool identity-prod fronts 4 members with weighted balancing, health probe https/8080 every 10s and idle timeout 900s; persistence cookie.

- (F00489) VLAN 2035 (app-mgmt) is trunked between eas-sw20 and ald-sw08 on port-channel 38, uses MTU 9000, maps to VRF MGMT-1 and runs MSTP with bridge priority 4096; changes require CAB approval 9 days ahead.

- (F00490) Load balancer pool mailer-dr fronts 7 members with round-robin balancing, health probe http/80 every 5s and idle timeout 300s; persistence cookie.

- (F00491) BGP peering between core-3 (AS 65098) and edge-1 (AS 65184) at Cresswick uses timers 30/90s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-MONITORING-3 applies.

- (F00492) Firewall rule 3171 permits udp/5432 from 10.131.7.0/24 to 10.57.89.0/26 with sampled logging; the rule is reviewed every 60 days by Service Delivery and expires on 2028-03-09.

- (F00493) Firewall rule 6617 permits tcp/8443 from 10.78.253.0/24 to 10.211.196.0/26 with full logging; the rule is reviewed every 180 days by Network Operations and expires on 2027-10-24.

- (F00494) BGP peering between core-1 (AS 64683) and edge-8 (AS 64920) at Dunmoor uses timers 10/30s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-CACHE-13 applies.

- (F00495) Load balancer pool reports-prod fronts 6 members with round-robin balancing, health probe http/8080 every 10s and idle timeout 60s; persistence none.

## Page 56: WAN links [network]

- (F00496) BGP peering between core-6 (AS 64788) and edge-5 (AS 65333) at Aldermere uses timers 10/90s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-MONITORING-25 applies.

- (F00497) Firewall rule 9518 permits udp/6379 from 10.92.160.0/24 to 10.5.4.0/26 with full logging; the rule is reviewed every 30 days by Service Delivery and expires on 2027-09-04.

- (F00498) Load balancer pool telemetry-preprod fronts 2 members with least-connections balancing, health probe https/80 every 5s and idle timeout 240s; persistence cookie.

- (F00499) VLAN 632 (bastion-mgmt) is trunked between fer-sw04 and ald-sw20 on port-channel 12, uses MTU 1500, maps to VRF PREPROD-5 and runs MSTP with bridge priority 32768; changes require CAB approval 3 days ahead.

- (F00500) Load balancer pool mailer-test fronts 4 members with least-connections balancing, health probe http/80 every 10s and idle timeout 900s; persistence source-ip.

- (F00501) VLAN 384 (monitoring-preprod) is trunked between cre-sw09 and bri-sw15 on port-channel 40, uses MTU 9000, maps to VRF PREPROD-8 and runs RSTP with bridge priority 8192; changes require CAB approval 10 days ahead.

- (F00502) Load balancer pool identity-test fronts 3 members with least-connections balancing, health probe tcp/80 every 30s and idle timeout 300s; persistence source-ip.

- (F00503) VLAN 103 (web-dr) is trunked between dun-sw05 and fer-sw21 on port-channel 18, uses MTU 1500, maps to VRF TEST-7 and runs RSTP with bridge priority 32768; changes require CAB approval 9 days ahead.

- (F00504) Load balancer pool gateway-prod fronts 8 members with weighted balancing, health probe http/80 every 30s and idle timeout 300s; persistence source-ip.

## Page 57: Perimeter firewalls [network]

- (F00505) Load balancer pool mailer-mgmt fronts 7 members with least-connections balancing, health probe http/443 every 30s and idle timeout 240s; persistence none.

- (F00506) VLAN 2950 (bastion-prod) is trunked between dun-sw22 and bri-sw10 on port-channel 41, uses MTU 9216, maps to VRF TEST-8 and runs RSTP with bridge priority 32768; changes require CAB approval 5 days ahead.

- (F00507) Firewall rule 4907 permits udp/1433 from 10.32.157.0/24 to 10.255.230.0/26 with full logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2027-06-26.

- (F00508) VLAN 2833 (monitoring-mgmt) is trunked between dun-sw04 and bri-sw21 on port-channel 10, uses MTU 9216, maps to VRF MGMT-4 and runs RSTP with bridge priority 4096; changes require CAB approval 4 days ahead.

- (F00509) Load balancer pool ledger-preprod fronts 12 members with least-connections balancing, health probe tcp/80 every 30s and idle timeout 60s; persistence source-ip.

- (F00510) VLAN 361 (app-prod) is trunked between dun-sw20 and bri-sw19 on port-channel 32, uses MTU 9216, maps to VRF MGMT-4 and runs RSTP with bridge priority 8192; changes require CAB approval 8 days ahead.

- (F00511) BGP peering between core-2 (AS 65511) and edge-3 (AS 64841) at Brightholm uses timers 3/90s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-APP-4 applies.

- (F00512) BGP peering between core-6 (AS 65078) and edge-3 (AS 64961) at Brightholm uses timers 30/9s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-BASTION-25 applies.

- (F00513) Firewall rule 1118 permits tcp/443 from 10.145.213.0/24 to 10.243.64.0/26 with full logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2029-08-14.

## Page 58: Switching fabric [network]

- (F00514) Firewall rule 3949 permits udp/9092 from 10.45.154.0/24 to 10.178.214.0/26 with full logging; the rule is reviewed every 60 days by Network Operations and expires on 2027-09-04.

- (F00515) BGP peering between core-4 (AS 64795) and edge-1 (AS 64710) at Aldermere uses timers 3/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-DATA-6 applies.

- (F00516) VLAN 958 (bastion-test) is trunked between ald-sw21 and cre-sw10 on port-channel 22, uses MTU 9216, maps to VRF DR-1 and runs RSTP with bridge priority 4096; changes require CAB approval 10 days ahead.

- (F00517) Firewall rule 2901 permits tcp/8443 from 10.227.166.0/24 to 10.214.101.0/26 with sampled logging; the rule is reviewed every 90 days by Network Operations and expires on 2027-06-08.

- (F00518) VLAN 1638 (cache-prod) is trunked between bri-sw24 and dun-sw07 on port-channel 31, uses MTU 9216, maps to VRF DR-1 and runs MSTP with bridge priority 8192; changes require CAB approval 5 days ahead.

- (F00519) Load balancer pool identity-preprod fronts 12 members with round-robin balancing, health probe http/80 every 10s and idle timeout 240s; persistence none.

- (F00520) VLAN 1978 (bastion-preprod) is trunked between cre-sw05 and ald-sw15 on port-channel 22, uses MTU 1500, maps to VRF TEST-3 and runs RSTP with bridge priority 8192; changes require CAB approval 3 days ahead.

- (F00521) Load balancer pool identity-dr fronts 6 members with least-connections balancing, health probe https/443 every 30s and idle timeout 240s; persistence none.

- (F00522) BGP peering between core-3 (AS 65447) and edge-1 (AS 64939) at Aldermere uses timers 3/30s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-WEB-14 applies.

## Page 59: WAN links [network]

- (F00523) Load balancer pool identity-preprod fronts 3 members with weighted balancing, health probe tcp/8080 every 30s and idle timeout 900s; persistence none.

- (F00524) Firewall rule 2486 permits tcp/1433 from 10.156.82.0/24 to 10.235.12.0/26 with drop-only logging; the rule is reviewed every 180 days by Network Operations and expires on 2029-07-06.

- (F00525) BGP peering between core-1 (AS 65393) and edge-2 (AS 64906) at Fernhollow uses timers 10/90s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-BASTION-25 applies.

- (F00526) BGP peering between core-4 (AS 65318) and edge-2 (AS 65147) at Cresswick uses timers 30/9s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-BATCH-29 applies.

- (F00527) VLAN 2635 (web-test) is trunked between ald-sw13 and cre-sw15 on port-channel 24, uses MTU 1500, maps to VRF MGMT-2 and runs RSTP with bridge priority 8192; changes require CAB approval 7 days ahead.

- (F00528) Firewall rule 4437 permits tcp/5432 from 10.180.136.0/24 to 10.216.141.0/26 with full logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2028-08-16.

- (F00529) VLAN 3480 (queue-dr) is trunked between dun-sw23 and eas-sw22 on port-channel 40, uses MTU 9000, maps to VRF PROD-4 and runs MSTP with bridge priority 4096; changes require CAB approval 3 days ahead.

- (F00530) Load balancer pool scheduler-test fronts 3 members with weighted balancing, health probe tcp/443 every 5s and idle timeout 240s; persistence cookie.

- (F00531) VLAN 3916 (data-dr) is trunked between cre-sw14 and fer-sw18 on port-channel 23, uses MTU 9000, maps to VRF DR-1 and runs MSTP with bridge priority 8192; changes require CAB approval 3 days ahead.

## Page 60: Core routing [network]

- (F00532) Firewall rule 6616 permits udp/1433 from 10.227.234.0/24 to 10.155.67.0/26 with drop-only logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2027-08-12.

- (F00533) BGP peering between core-8 (AS 65491) and edge-3 (AS 65145) at Brightholm uses timers 30/90s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-DATA-27 applies.

- (F00534) Firewall rule 6187 permits tcp/1433 from 10.133.189.0/24 to 10.94.105.0/26 with sampled logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2028-03-12.

- (F00535) Load balancer pool catalogue-prod fronts 8 members with round-robin balancing, health probe tcp/443 every 10s and idle timeout 240s; persistence none.

- (F00536) BGP peering between core-5 (AS 65504) and edge-3 (AS 65330) at Eastvale uses timers 30/30s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-APP-24 applies.

- (F00537) Load balancer pool catalogue-test fronts 2 members with round-robin balancing, health probe https/80 every 10s and idle timeout 300s; persistence none.

- (F00538) BGP peering between core-4 (AS 65312) and edge-5 (AS 64712) at Aldermere uses timers 3/90s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-APP-17 applies.

- (F00539) Load balancer pool ledger-test fronts 8 members with least-connections balancing, health probe https/443 every 10s and idle timeout 900s; persistence source-ip.

- (F00540) VLAN 1925 (app-preprod) is trunked between cre-sw12 and cre-sw10 on port-channel 47, uses MTU 9000, maps to VRF DR-8 and runs MSTP with bridge priority 8192; changes require CAB approval 8 days ahead.

## Page 61: Load balancing [network]

- (F00541) Firewall rule 4404 permits udp/1433 from 10.171.33.0/24 to 10.192.45.0/26 with full logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2028-03-18.

- (F00542) Load balancer pool scheduler-dr fronts 6 members with weighted balancing, health probe http/80 every 10s and idle timeout 300s; persistence source-ip.

- (F00543) Load balancer pool telemetry-test fronts 12 members with weighted balancing, health probe http/80 every 30s and idle timeout 300s; persistence source-ip.

- (F00544) Firewall rule 1466 permits tcp/5432 from 10.252.34.0/24 to 10.185.246.0/26 with sampled logging; the rule is reviewed every 180 days by Infrastructure Architecture and expires on 2029-11-16.

- (F00545) VLAN 171 (queue-preprod) is trunked between cre-sw17 and fer-sw19 on port-channel 38, uses MTU 1500, maps to VRF PREPROD-6 and runs MSTP with bridge priority 8192; changes require CAB approval 7 days ahead.

- (F00546) Firewall rule 6832 permits tcp/5432 from 10.149.39.0/24 to 10.99.93.0/26 with full logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2028-11-26.

- (F00547) BGP peering between core-6 (AS 64610) and edge-6 (AS 65355) at Brightholm uses timers 3/9s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-BATCH-25 applies.

- (F00548) Load balancer pool gateway-preprod fronts 10 members with least-connections balancing, health probe tcp/8080 every 30s and idle timeout 60s; persistence source-ip.

- (F00549) Load balancer pool identity-test fronts 6 members with weighted balancing, health probe http/80 every 10s and idle timeout 300s; persistence none.

## Page 62: Perimeter firewalls [network]

- (F00550) VLAN 3609 (data-preprod) is trunked between fer-sw04 and bri-sw05 on port-channel 20, uses MTU 1500, maps to VRF PREPROD-3 and runs RSTP with bridge priority 32768; changes require CAB approval 3 days ahead.

- (F00551) VLAN 904 (app-prod) is trunked between ald-sw16 and dun-sw02 on port-channel 43, uses MTU 9216, maps to VRF MGMT-1 and runs MSTP with bridge priority 4096; changes require CAB approval 6 days ahead.

- (F00552) VLAN 3190 (app-prod) is trunked between ald-sw10 and fer-sw01 on port-channel 39, uses MTU 1500, maps to VRF MGMT-4 and runs RSTP with bridge priority 24576; changes require CAB approval 2 days ahead.

- (F00553) VLAN 1524 (batch-preprod) is trunked between bri-sw24 and cre-sw19 on port-channel 33, uses MTU 9216, maps to VRF MGMT-4 and runs RSTP with bridge priority 4096; changes require CAB approval 2 days ahead.

- (F00554) Firewall rule 9800 permits tcp/6379 from 10.50.109.0/24 to 10.243.187.0/26 with sampled logging; the rule is reviewed every 60 days by Service Delivery and expires on 2029-02-06.

- (F00555) BGP peering between core-4 (AS 64929) and edge-2 (AS 65291) at Cresswick uses timers 3/30s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-DATA-16 applies.

- (F00556) BGP peering between core-1 (AS 64596) and edge-6 (AS 65017) at Aldermere uses timers 10/30s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-QUEUE-22 applies.

- (F00557) Load balancer pool reports-preprod fronts 3 members with round-robin balancing, health probe https/443 every 5s and idle timeout 60s; persistence cookie.

- (F00558) Load balancer pool catalogue-prod fronts 4 members with round-robin balancing, health probe http/8080 every 30s and idle timeout 60s; persistence cookie.

## Page 63: Switching fabric [network]

- (F00559) VLAN 2536 (bastion-prod) is trunked between cre-sw07 and cre-sw07 on port-channel 15, uses MTU 9000, maps to VRF DR-5 and runs MSTP with bridge priority 32768; changes require CAB approval 7 days ahead.

- (F00560) Load balancer pool telemetry-preprod fronts 9 members with least-connections balancing, health probe tcp/443 every 10s and idle timeout 900s; persistence none.

- (F00561) Firewall rule 2117 permits udp/6379 from 10.13.91.0/24 to 10.195.167.0/26 with full logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2027-11-25.

- (F00562) Load balancer pool identity-dr fronts 10 members with round-robin balancing, health probe https/443 every 30s and idle timeout 60s; persistence none.

- (F00563) Load balancer pool reports-dr fronts 9 members with least-connections balancing, health probe tcp/80 every 30s and idle timeout 300s; persistence cookie.

- (F00564) Firewall rule 7374 permits udp/443 from 10.251.240.0/24 to 10.243.80.0/26 with sampled logging; the rule is reviewed every 30 days by Service Delivery and expires on 2028-08-19.

- (F00565) Load balancer pool mailer-prod fronts 2 members with weighted balancing, health probe tcp/80 every 10s and idle timeout 300s; persistence cookie.

- (F00566) VLAN 1853 (batch-test) is trunked between fer-sw11 and dun-sw04 on port-channel 27, uses MTU 9000, maps to VRF PROD-4 and runs RSTP with bridge priority 8192; changes require CAB approval 6 days ahead.

- (F00567) VLAN 1482 (data-prod) is trunked between fer-sw03 and cre-sw04 on port-channel 35, uses MTU 9000, maps to VRF PROD-8 and runs MSTP with bridge priority 32768; changes require CAB approval 6 days ahead.

## Page 64: Core routing [network]

- (F00568) Load balancer pool reports-test fronts 11 members with least-connections balancing, health probe http/80 every 30s and idle timeout 240s; persistence source-ip.

- (F00569) Load balancer pool telemetry-test fronts 8 members with least-connections balancing, health probe http/8080 every 5s and idle timeout 240s; persistence source-ip.

- (F00570) BGP peering between core-4 (AS 65151) and edge-2 (AS 65246) at Eastvale uses timers 3/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-APP-19 applies.

- (F00571) Load balancer pool telemetry-mgmt fronts 6 members with round-robin balancing, health probe https/8080 every 10s and idle timeout 240s; persistence source-ip.

- (F00572) Load balancer pool scheduler-prod fronts 12 members with weighted balancing, health probe https/80 every 30s and idle timeout 900s; persistence none.

- (F00573) Load balancer pool reports-mgmt fronts 12 members with least-connections balancing, health probe https/80 every 10s and idle timeout 900s; persistence none.

- (F00574) Firewall rule 8133 permits udp/5432 from 10.32.104.0/24 to 10.211.136.0/26 with drop-only logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2029-10-08.

- (F00575) Load balancer pool ledger-preprod fronts 6 members with round-robin balancing, health probe http/8080 every 10s and idle timeout 900s; persistence cookie.

- (F00576) VLAN 219 (queue-test) is trunked between bri-sw06 and cre-sw05 on port-channel 43, uses MTU 9216, maps to VRF PREPROD-1 and runs MSTP with bridge priority 4096; changes require CAB approval 2 days ahead.

## Page 65: Core routing [network]

- (F00577) BGP peering between core-6 (AS 65199) and edge-2 (AS 64918) at Fernhollow uses timers 3/9s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-APP-17 applies.

- (F00578) BGP peering between core-2 (AS 65303) and edge-6 (AS 64849) at Eastvale uses timers 30/30s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-CACHE-30 applies.

- (F00579) Load balancer pool gateway-test fronts 9 members with round-robin balancing, health probe http/8080 every 5s and idle timeout 900s; persistence cookie.

- (F00580) BGP peering between core-7 (AS 64998) and edge-4 (AS 65498) at Cresswick uses timers 3/30s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-BATCH-27 applies.

- (F00581) BGP peering between core-1 (AS 65219) and edge-4 (AS 64771) at Eastvale uses timers 10/30s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-BATCH-29 applies.

- (F00582) VLAN 132 (bastion-test) is trunked between eas-sw08 and dun-sw13 on port-channel 20, uses MTU 1500, maps to VRF PREPROD-5 and runs RSTP with bridge priority 8192; changes require CAB approval 9 days ahead.

- (F00583) BGP peering between core-2 (AS 65354) and edge-8 (AS 64994) at Fernhollow uses timers 10/30s, max-prefix 5000 and BFD interval 300 ms; ingress route-map RM-APP-27 applies.

- (F00584) Firewall rule 6764 permits udp/9092 from 10.167.232.0/24 to 10.14.26.0/26 with sampled logging; the rule is reviewed every 60 days by Service Delivery and expires on 2029-03-01.

- (F00585) Load balancer pool catalogue-prod fronts 4 members with least-connections balancing, health probe https/8080 every 30s and idle timeout 240s; persistence cookie.

## Page 66: Load balancing [network]

- (F00586) BGP peering between core-5 (AS 64689) and edge-6 (AS 65330) at Cresswick uses timers 3/9s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-DATA-13 applies.

- (F00587) Load balancer pool gateway-prod fronts 9 members with least-connections balancing, health probe http/8080 every 5s and idle timeout 60s; persistence source-ip.

- (F00588) Load balancer pool mailer-preprod fronts 11 members with least-connections balancing, health probe tcp/8080 every 30s and idle timeout 900s; persistence source-ip.

- (F00589) Load balancer pool gateway-test fronts 6 members with weighted balancing, health probe http/443 every 5s and idle timeout 900s; persistence none.

- (F00590) Firewall rule 7853 permits tcp/1433 from 10.74.14.0/24 to 10.148.134.0/26 with full logging; the rule is reviewed every 180 days by Network Operations and expires on 2028-10-22.

- (F00591) Load balancer pool mailer-dr fronts 12 members with least-connections balancing, health probe https/443 every 30s and idle timeout 900s; persistence cookie.

- (F00592) BGP peering between core-1 (AS 64852) and edge-4 (AS 64994) at Cresswick uses timers 30/90s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-WEB-1 applies.

- (F00593) BGP peering between core-7 (AS 65199) and edge-6 (AS 64647) at Eastvale uses timers 3/90s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-DATA-17 applies.

- (F00594) Load balancer pool mailer-mgmt fronts 8 members with least-connections balancing, health probe http/80 every 10s and idle timeout 60s; persistence none.

## Page 67: Load balancing [network]

- (F00595) BGP peering between core-5 (AS 65139) and edge-5 (AS 65041) at Cresswick uses timers 10/9s, max-prefix 1000 and BFD interval 500 ms; ingress route-map RM-MONITORING-25 applies.

- (F00596) Firewall rule 1871 permits tcp/8443 from 10.27.117.0/24 to 10.93.18.0/26 with drop-only logging; the rule is reviewed every 90 days by Network Operations and expires on 2029-08-14.

- (F00597) VLAN 3004 (monitoring-dr) is trunked between dun-sw02 and dun-sw12 on port-channel 32, uses MTU 1500, maps to VRF PREPROD-2 and runs MSTP with bridge priority 4096; changes require CAB approval 5 days ahead.

- (F00598) BGP peering between core-5 (AS 65088) and edge-4 (AS 65109) at Aldermere uses timers 30/90s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-APP-8 applies.

- (F00599) Load balancer pool telemetry-prod fronts 8 members with round-robin balancing, health probe https/80 every 10s and idle timeout 240s; persistence none.

- (F00600) VLAN 1959 (queue-mgmt) is trunked between dun-sw23 and fer-sw16 on port-channel 43, uses MTU 1500, maps to VRF TEST-1 and runs MSTP with bridge priority 24576; changes require CAB approval 4 days ahead.

- (F00601) Firewall rule 1909 permits tcp/9092 from 10.195.47.0/24 to 10.204.130.0/26 with full logging; the rule is reviewed every 60 days by Service Delivery and expires on 2027-01-28.

- (F00602) Firewall rule 3525 permits tcp/5432 from 10.251.221.0/24 to 10.158.67.0/26 with drop-only logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2029-04-16.

- (F00603) Load balancer pool reports-prod fronts 8 members with round-robin balancing, health probe https/80 every 10s and idle timeout 900s; persistence none.

## Page 68: Core routing [network]

- (F00604) BGP peering between core-3 (AS 65465) and edge-8 (AS 65051) at Fernhollow uses timers 30/90s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-MONITORING-14 applies.

- (F00605) VLAN 2902 (queue-preprod) is trunked between dun-sw10 and bri-sw05 on port-channel 34, uses MTU 9000, maps to VRF TEST-1 and runs RSTP with bridge priority 4096; changes require CAB approval 10 days ahead.

- (F00606) VLAN 2003 (queue-test) is trunked between eas-sw14 and dun-sw04 on port-channel 17, uses MTU 9216, maps to VRF PROD-9 and runs RSTP with bridge priority 4096; changes require CAB approval 9 days ahead.

- (F00607) Firewall rule 7819 permits udp/5432 from 10.232.230.0/24 to 10.135.174.0/26 with full logging; the rule is reviewed every 60 days by Network Operations and expires on 2027-12-20.

- (F00608) BGP peering between core-1 (AS 64517) and edge-7 (AS 64631) at Aldermere uses timers 3/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-BASTION-28 applies.

- (F00609) Load balancer pool reports-test fronts 3 members with least-connections balancing, health probe tcp/80 every 5s and idle timeout 60s; persistence none.

- (F00610) Firewall rule 3378 permits tcp/1433 from 10.97.44.0/24 to 10.154.237.0/26 with full logging; the rule is reviewed every 180 days by Service Delivery and expires on 2027-02-06.

- (F00611) Firewall rule 8724 permits tcp/1433 from 10.124.103.0/24 to 10.150.200.0/26 with full logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2027-11-28.

- (F00612) Load balancer pool telemetry-prod fronts 9 members with round-robin balancing, health probe http/8080 every 30s and idle timeout 900s; persistence none.

## Page 69: Core routing [network]

- (F00613) VLAN 360 (queue-dr) is trunked between dun-sw19 and cre-sw18 on port-channel 31, uses MTU 1500, maps to VRF DR-6 and runs MSTP with bridge priority 32768; changes require CAB approval 2 days ahead.

- (F00614) Firewall rule 6633 permits udp/8443 from 10.112.173.0/24 to 10.239.67.0/26 with drop-only logging; the rule is reviewed every 180 days by Service Delivery and expires on 2029-11-24.

- (F00615) BGP peering between core-5 (AS 65219) and edge-2 (AS 65195) at Dunmoor uses timers 3/9s, max-prefix 500 and BFD interval 100 ms; ingress route-map RM-MONITORING-4 applies.

- (F00616) Load balancer pool ledger-prod fronts 7 members with round-robin balancing, health probe http/8080 every 5s and idle timeout 240s; persistence cookie.

- (F00617) VLAN 2629 (cache-prod) is trunked between ald-sw11 and dun-sw04 on port-channel 36, uses MTU 1500, maps to VRF DR-5 and runs MSTP with bridge priority 24576; changes require CAB approval 2 days ahead.

- (F00618) BGP peering between core-2 (AS 65235) and edge-1 (AS 65460) at Dunmoor uses timers 10/9s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-APP-27 applies.

- (F00619) VLAN 583 (cache-test) is trunked between eas-sw04 and bri-sw21 on port-channel 11, uses MTU 9216, maps to VRF TEST-8 and runs MSTP with bridge priority 4096; changes require CAB approval 4 days ahead.

- (F00620) BGP peering between core-8 (AS 65504) and edge-7 (AS 65299) at Aldermere uses timers 3/30s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-DATA-3 applies.

- (F00621) BGP peering between core-4 (AS 64667) and edge-7 (AS 65318) at Brightholm uses timers 3/30s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-MONITORING-28 applies.

## Page 70: WAN links [network]

- (F00622) BGP peering between core-2 (AS 64598) and edge-6 (AS 64834) at Dunmoor uses timers 3/30s, max-prefix 500 and BFD interval 300 ms; ingress route-map RM-WEB-22 applies.

- (F00623) Firewall rule 9516 permits udp/1433 from 10.205.155.0/24 to 10.160.176.0/26 with full logging; the rule is reviewed every 90 days by Network Operations and expires on 2029-07-15.

- (F00624) Firewall rule 8244 permits udp/6379 from 10.207.101.0/24 to 10.154.43.0/26 with full logging; the rule is reviewed every 90 days by Service Delivery and expires on 2029-12-24.

- (F00625) Firewall rule 2520 permits udp/9092 from 10.174.81.0/24 to 10.11.14.0/26 with sampled logging; the rule is reviewed every 90 days by Network Operations and expires on 2028-12-14.

- (F00626) VLAN 2668 (batch-prod) is trunked between fer-sw02 and cre-sw09 on port-channel 4, uses MTU 9216, maps to VRF PROD-8 and runs MSTP with bridge priority 4096; changes require CAB approval 9 days ahead.

- (F00627) BGP peering between core-4 (AS 64870) and edge-5 (AS 64803) at Fernhollow uses timers 30/90s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-BASTION-17 applies.

- (F00628) Firewall rule 4154 permits udp/1433 from 10.50.75.0/24 to 10.217.210.0/26 with full logging; the rule is reviewed every 30 days by Platform Engineering and expires on 2028-03-16.

- (F00629) Firewall rule 9622 permits udp/9092 from 10.202.135.0/24 to 10.255.216.0/26 with drop-only logging; the rule is reviewed every 180 days by Service Delivery and expires on 2027-03-17.

- (F00630) Firewall rule 9408 permits tcp/6379 from 10.108.233.0/24 to 10.242.16.0/26 with sampled logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2027-10-28.

## Page 71: Load balancing [network]

- (F00631) VLAN 264 (data-prod) is trunked between ald-sw12 and eas-sw10 on port-channel 24, uses MTU 9000, maps to VRF TEST-5 and runs MSTP with bridge priority 32768; changes require CAB approval 2 days ahead.

- (F00632) Firewall rule 5999 permits udp/8443 from 10.93.250.0/24 to 10.1.62.0/26 with sampled logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2027-07-16.

- (F00633) BGP peering between core-8 (AS 65366) and edge-3 (AS 65292) at Brightholm uses timers 30/90s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-MONITORING-5 applies.

- (F00634) BGP peering between core-7 (AS 64908) and edge-4 (AS 65433) at Dunmoor uses timers 10/90s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-MONITORING-24 applies.

- (F00635) BGP peering between core-1 (AS 65097) and edge-5 (AS 65086) at Fernhollow uses timers 3/90s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-CACHE-20 applies.

- (F00636) VLAN 2158 (web-prod) is trunked between eas-sw17 and bri-sw16 on port-channel 43, uses MTU 9216, maps to VRF PREPROD-1 and runs MSTP with bridge priority 8192; changes require CAB approval 5 days ahead.

- (F00637) Load balancer pool reports-mgmt fronts 2 members with round-robin balancing, health probe tcp/443 every 10s and idle timeout 240s; persistence source-ip.

- (F00638) VLAN 472 (app-prod) is trunked between eas-sw11 and dun-sw09 on port-channel 35, uses MTU 1500, maps to VRF TEST-3 and runs RSTP with bridge priority 24576; changes require CAB approval 3 days ahead.

- (F00639) Firewall rule 1965 permits udp/8443 from 10.13.29.0/24 to 10.152.199.0/26 with full logging; the rule is reviewed every 90 days by Network Operations and expires on 2028-06-09.

## Page 72: Load balancing [network]

- (F00640) VLAN 2500 (cache-dr) is trunked between ald-sw07 and bri-sw20 on port-channel 33, uses MTU 9216, maps to VRF DR-2 and runs MSTP with bridge priority 4096; changes require CAB approval 7 days ahead.

- (F00641) Load balancer pool ledger-dr fronts 12 members with least-connections balancing, health probe tcp/443 every 30s and idle timeout 60s; persistence none.

- (F00642) Firewall rule 2374 permits tcp/8443 from 10.191.86.0/24 to 10.125.216.0/26 with sampled logging; the rule is reviewed every 180 days by Platform Engineering and expires on 2027-08-27.

- (F00643) BGP peering between core-8 (AS 64791) and edge-5 (AS 65371) at Fernhollow uses timers 10/30s, max-prefix 5000 and BFD interval 100 ms; ingress route-map RM-QUEUE-2 applies.

- (F00644) Firewall rule 5925 permits tcp/1433 from 10.62.71.0/24 to 10.143.221.0/26 with full logging; the rule is reviewed every 90 days by Infrastructure Architecture and expires on 2029-05-25.

- (F00645) Load balancer pool mailer-preprod fronts 9 members with weighted balancing, health probe http/80 every 30s and idle timeout 240s; persistence cookie.

- (F00646) VLAN 2855 (data-dr) is trunked between eas-sw16 and ald-sw01 on port-channel 36, uses MTU 9216, maps to VRF DR-7 and runs RSTP with bridge priority 4096; changes require CAB approval 10 days ahead.

- (F00647) VLAN 1545 (bastion-mgmt) is trunked between fer-sw15 and fer-sw04 on port-channel 23, uses MTU 9000, maps to VRF PREPROD-1 and runs RSTP with bridge priority 32768; changes require CAB approval 7 days ahead.

- (F00648) Firewall rule 1324 permits udp/6379 from 10.183.98.0/24 to 10.46.155.0/26 with sampled logging; the rule is reviewed every 60 days by Network Operations and expires on 2028-06-02.

## Page 73: Perimeter firewalls [network]

- (F00649) Load balancer pool ledger-preprod fronts 12 members with round-robin balancing, health probe tcp/443 every 30s and idle timeout 900s; persistence none.

- (F00650) Firewall rule 3875 permits tcp/9092 from 10.65.33.0/24 to 10.65.132.0/26 with sampled logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2027-11-01.

- (F00651) BGP peering between core-7 (AS 65168) and edge-1 (AS 65386) at Cresswick uses timers 10/30s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-MONITORING-16 applies.

- (F00652) BGP peering between core-1 (AS 64796) and edge-7 (AS 65057) at Dunmoor uses timers 10/9s, max-prefix 1000 and BFD interval 100 ms; ingress route-map RM-BATCH-3 applies.

- (F00653) VLAN 404 (cache-preprod) is trunked between fer-sw08 and fer-sw14 on port-channel 11, uses MTU 9000, maps to VRF TEST-2 and runs RSTP with bridge priority 4096; changes require CAB approval 9 days ahead.

- (F00654) Load balancer pool telemetry-preprod fronts 3 members with round-robin balancing, health probe tcp/443 every 5s and idle timeout 300s; persistence cookie.

- (F00655) Firewall rule 2567 permits udp/9092 from 10.63.43.0/24 to 10.31.17.0/26 with drop-only logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2027-01-26.

- (F00656) Load balancer pool reports-prod fronts 3 members with weighted balancing, health probe tcp/8080 every 5s and idle timeout 300s; persistence source-ip.

- (F00657) Load balancer pool ledger-dr fronts 8 members with round-robin balancing, health probe http/8080 every 30s and idle timeout 60s; persistence source-ip.

## Page 74: Core routing [network]

- (F00658) Load balancer pool catalogue-prod fronts 2 members with weighted balancing, health probe https/80 every 30s and idle timeout 240s; persistence cookie.

- (F00659) Firewall rule 7897 permits udp/6379 from 10.227.95.0/24 to 10.124.70.0/26 with full logging; the rule is reviewed every 30 days by Network Operations and expires on 2028-10-14.

- (F00660) BGP peering between core-3 (AS 64992) and edge-5 (AS 65129) at Cresswick uses timers 10/30s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-DATA-2 applies.

- (F00661) Firewall rule 6633 permits tcp/8443 from 10.103.35.0/24 to 10.174.96.0/26 with sampled logging; the rule is reviewed every 180 days by Service Delivery and expires on 2029-12-11.

- (F00662) BGP peering between core-3 (AS 64619) and edge-8 (AS 65409) at Aldermere uses timers 10/9s, max-prefix 500 and BFD interval 500 ms; ingress route-map RM-CACHE-23 applies.

- (F00663) Firewall rule 8876 permits udp/6379 from 10.192.105.0/24 to 10.204.94.0/26 with full logging; the rule is reviewed every 90 days by Platform Engineering and expires on 2027-06-01.

- (F00664) VLAN 2685 (batch-prod) is trunked between bri-sw10 and dun-sw07 on port-channel 2, uses MTU 1500, maps to VRF PREPROD-5 and runs RSTP with bridge priority 8192; changes require CAB approval 6 days ahead.

- (F00665) Firewall rule 4211 permits tcp/8443 from 10.134.51.0/24 to 10.10.70.0/26 with drop-only logging; the rule is reviewed every 30 days by Infrastructure Architecture and expires on 2027-05-15.

- (F00666) Firewall rule 9633 permits udp/6379 from 10.33.60.0/24 to 10.73.66.0/26 with full logging; the rule is reviewed every 60 days by Service Delivery and expires on 2029-06-11.

## Page 75: WAN links [network]

- (F00667) Load balancer pool gateway-mgmt fronts 6 members with least-connections balancing, health probe http/80 every 5s and idle timeout 300s; persistence none.

- (F00668) Load balancer pool catalogue-preprod fronts 10 members with round-robin balancing, health probe https/8080 every 10s and idle timeout 900s; persistence cookie.

- (F00669) Load balancer pool identity-dr fronts 9 members with round-robin balancing, health probe https/443 every 30s and idle timeout 60s; persistence none.

- (F00670) Firewall rule 4581 permits udp/1433 from 10.193.80.0/24 to 10.191.130.0/26 with sampled logging; the rule is reviewed every 30 days by Network Operations and expires on 2027-05-15.

- (F00671) BGP peering between core-6 (AS 64948) and edge-8 (AS 64990) at Dunmoor uses timers 10/30s, max-prefix 1000 and BFD interval 300 ms; ingress route-map RM-QUEUE-13 applies.

- (F00672) VLAN 2743 (app-test) is trunked between bri-sw15 and bri-sw09 on port-channel 6, uses MTU 9000, maps to VRF MGMT-9 and runs RSTP with bridge priority 24576; changes require CAB approval 5 days ahead.

- (F00673) VLAN 2336 (cache-test) is trunked between ald-sw03 and cre-sw02 on port-channel 13, uses MTU 9216, maps to VRF TEST-5 and runs MSTP with bridge priority 24576; changes require CAB approval 5 days ahead.

- (F00674) Firewall rule 1139 permits udp/5432 from 10.177.206.0/24 to 10.207.6.0/26 with drop-only logging; the rule is reviewed every 60 days by Service Delivery and expires on 2027-04-24.

- (F00675) Firewall rule 8679 permits udp/5432 from 10.43.160.0/24 to 10.96.219.0/26 with sampled logging; the rule is reviewed every 180 days by Network Operations and expires on 2028-08-28.

## Page 76: WAN links [network]

- (F00676) VLAN 1351 (web-dr) is trunked between cre-sw05 and eas-sw05 on port-channel 43, uses MTU 9000, maps to VRF TEST-4 and runs MSTP with bridge priority 32768; changes require CAB approval 8 days ahead.

- (F00677) BGP peering between core-1 (AS 65456) and edge-3 (AS 64669) at Cresswick uses timers 30/90s, max-prefix 5000 and BFD interval 500 ms; ingress route-map RM-BASTION-13 applies.

- (F00678) Firewall rule 4085 permits udp/443 from 10.168.231.0/24 to 10.155.47.0/26 with full logging; the rule is reviewed every 30 days by Network Operations and expires on 2027-12-20.

- (F00679) Load balancer pool reports-test fronts 5 members with least-connections balancing, health probe http/8080 every 30s and idle timeout 60s; persistence source-ip.

- (F00680) VLAN 1438 (bastion-dr) is trunked between cre-sw17 and ald-sw06 on port-channel 11, uses MTU 1500, maps to VRF PREPROD-9 and runs MSTP with bridge priority 32768; changes require CAB approval 3 days ahead.

- (F00681) Load balancer pool reports-dr fronts 4 members with weighted balancing, health probe https/443 every 30s and idle timeout 240s; persistence cookie.

- (F00682) Load balancer pool identity-prod fronts 8 members with weighted balancing, health probe tcp/8080 every 10s and idle timeout 900s; persistence source-ip.

- (F00683) Load balancer pool telemetry-dr fronts 7 members with weighted balancing, health probe https/443 every 10s and idle timeout 240s; persistence source-ip.

- (F00684) Firewall rule 8501 permits udp/6379 from 10.93.48.0/24 to 10.201.22.0/26 with full logging; the rule is reviewed every 60 days by Infrastructure Architecture and expires on 2029-09-10.

## Page 77: IPv4 supernets [addressing]

- (F00685) NAT pool 10.252.210.0/28 serves outbound traffic for catalogue in Fernhollow, supports 24665 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00686) NAT pool 10.230.84.0/28 serves outbound traffic for telemetry in Cresswick, supports 14090 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00687) Supernet 10.236.192.0/20 is delegated to Aldermere (prod) and summarised at border-3; the overlap check against Fernhollow passed in review 508, and 6 exceptions are documented in IPAM ticket IPAM-4185.

- (F00688) Supernet 10.58.64.0/18 is delegated to Aldermere (prod) and summarised at border-3; the overlap check against Fernhollow passed in review 866, and 3 exceptions are documented in IPAM ticket IPAM-8942.

- (F00689) Supernet 10.124.224.0/20 is delegated to Aldermere (prod) and summarised at border-2; the overlap check against Dunmoor passed in review 940, and 2 exceptions are documented in IPAM ticket IPAM-3643.

- (F00690) Subnet 10.90.148.0/22 is allocated to app workloads in Aldermere/mgmt; gateway .1, 19 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 13% at last audit.

- (F00691) NAT pool 10.225.183.0/28 serves outbound traffic for scheduler in Cresswick, supports 14699 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00692) NAT pool 10.226.24.0/28 serves outbound traffic for catalogue in Eastvale, supports 26099 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00693) Supernet 10.24.0.0/16 is delegated to Aldermere (mgmt) and summarised at border-2; the overlap check against Brightholm passed in review 483, and 1 exceptions are documented in IPAM ticket IPAM-4276.

## Page 78: IPv4 supernets [addressing]

- (F00694) Subnet 10.172.96.0/22 is allocated to app workloads in Dunmoor/prod; gateway .1, 9 addresses reserved, DHCP relay to dhcp-1, growth headroom 20% and utilisation 33% at last audit.

- (F00695) Subnet 10.167.164.0/22 is allocated to cache workloads in Dunmoor/mgmt; gateway .1, 8 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 41% at last audit.

- (F00696) Subnet 10.88.7.0/24 is allocated to bastion workloads in Aldermere/test; gateway .1, 12 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 70% at last audit.

- (F00697) Subnet 10.188.22.0/26 is allocated to app workloads in Aldermere/test; gateway .1, 8 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 25% at last audit.

- (F00698) NAT pool 10.87.128.0/28 serves outbound traffic for catalogue in Eastvale, supports 39812 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00699) NAT pool 10.170.89.0/28 serves outbound traffic for mailer in Dunmoor, supports 56307 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00700) Subnet 10.229.195.0/26 is allocated to cache workloads in Cresswick/prod; gateway .1, 18 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 27% at last audit.

- (F00701) Supernet 10.40.0.0/16 is delegated to Brightholm (dr) and summarised at border-2; the overlap check against Cresswick passed in review 610, and 2 exceptions are documented in IPAM ticket IPAM-4309.

- (F00702) Subnet 10.19.121.0/26 is allocated to monitoring workloads in Dunmoor/preprod; gateway .1, 12 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 17% at last audit.

## Page 79: NAT pools [addressing]

- (F00703) Supernet 10.117.0.0/16 is delegated to Fernhollow (test) and summarised at border-3; the overlap check against Brightholm passed in review 310, and 4 exceptions are documented in IPAM ticket IPAM-1885.

- (F00704) NAT pool 10.195.164.0/28 serves outbound traffic for scheduler in Brightholm, supports 29490 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00705) Subnet 10.26.72.0/22 is allocated to cache workloads in Dunmoor/prod; gateway .1, 6 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 42% at last audit.

- (F00706) NAT pool 10.239.159.0/28 serves outbound traffic for scheduler in Aldermere, supports 47795 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00707) Supernet 10.155.0.0/16 is delegated to Brightholm (mgmt) and summarised at border-5; the overlap check against Dunmoor passed in review 750, and 1 exceptions are documented in IPAM ticket IPAM-5454.

- (F00708) Supernet 10.193.64.0/18 is delegated to Aldermere (test) and summarised at border-4; the overlap check against Dunmoor passed in review 532, and 4 exceptions are documented in IPAM ticket IPAM-8101.

- (F00709) Subnet 10.218.42.0/24 is allocated to queue workloads in Dunmoor/prod; gateway .1, 19 addresses reserved, DHCP relay to dhcp-2, growth headroom 20% and utilisation 44% at last audit.

- (F00710) Supernet 10.145.192.0/18 is delegated to Dunmoor (test) and summarised at border-5; the overlap check against Eastvale passed in review 592, and 0 exceptions are documented in IPAM ticket IPAM-6459.

- (F00711) Subnet 10.79.96.0/22 is allocated to web workloads in Fernhollow/dr; gateway .1, 2 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 65% at last audit.

## Page 80: Management ranges [addressing]

- (F00712) NAT pool 10.250.157.0/28 serves outbound traffic for catalogue in Cresswick, supports 27290 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00713) Supernet 10.223.0.0/16 is delegated to Eastvale (preprod) and summarised at border-6; the overlap check against Cresswick passed in review 621, and 5 exceptions are documented in IPAM ticket IPAM-9005.

- (F00714) NAT pool 10.29.197.0/28 serves outbound traffic for reports in Fernhollow, supports 48712 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00715) Supernet 10.14.64.0/20 is delegated to Aldermere (test) and summarised at border-3; the overlap check against Eastvale passed in review 566, and 5 exceptions are documented in IPAM ticket IPAM-3414.

- (F00716) Supernet 10.82.0.0/20 is delegated to Brightholm (mgmt) and summarised at border-1; the overlap check against Aldermere passed in review 759, and 5 exceptions are documented in IPAM ticket IPAM-7297.

- (F00717) Supernet 10.96.0.0/16 is delegated to Fernhollow (mgmt) and summarised at border-2; the overlap check against Dunmoor passed in review 358, and 5 exceptions are documented in IPAM ticket IPAM-5951.

- (F00718) NAT pool 10.157.210.0/28 serves outbound traffic for catalogue in Eastvale, supports 7661 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00719) Supernet 10.107.192.0/20 is delegated to Brightholm (test) and summarised at border-6; the overlap check against Cresswick passed in review 106, and 1 exceptions are documented in IPAM ticket IPAM-9056.

- (F00720) Subnet 10.213.213.0/26 is allocated to queue workloads in Aldermere/prod; gateway .1, 15 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 35% at last audit.

## Page 81: Site allocations [addressing]

- (F00721) Subnet 10.56.230.0/26 is allocated to cache workloads in Dunmoor/preprod; gateway .1, 7 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 36% at last audit.

- (F00722) Supernet 10.55.80.0/20 is delegated to Dunmoor (dr) and summarised at border-1; the overlap check against Cresswick passed in review 187, and 3 exceptions are documented in IPAM ticket IPAM-3042.

- (F00723) Supernet 10.120.0.0/16 is delegated to Aldermere (test) and summarised at border-4; the overlap check against Fernhollow passed in review 878, and 0 exceptions are documented in IPAM ticket IPAM-1155.

- (F00724) Subnet 10.21.49.0/26 is allocated to cache workloads in Cresswick/prod; gateway .1, 18 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 74% at last audit.

- (F00725) Supernet 10.172.128.0/18 is delegated to Cresswick (mgmt) and summarised at border-6; the overlap check against Cresswick passed in review 422, and 6 exceptions are documented in IPAM ticket IPAM-4925.

- (F00726) Supernet 10.29.128.0/18 is delegated to Fernhollow (dr) and summarised at border-3; the overlap check against Aldermere passed in review 103, and 3 exceptions are documented in IPAM ticket IPAM-7583.

- (F00727) NAT pool 10.62.143.0/28 serves outbound traffic for gateway in Brightholm, supports 24645 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00728) NAT pool 10.211.96.0/28 serves outbound traffic for ledger in Fernhollow, supports 42316 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00729) NAT pool 10.166.227.0/28 serves outbound traffic for gateway in Cresswick, supports 40264 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

## Page 82: NAT pools [addressing]

- (F00730) Subnet 10.51.197.0/24 is allocated to queue workloads in Cresswick/dr; gateway .1, 8 addresses reserved, DHCP relay to dhcp-2, growth headroom 15% and utilisation 28% at last audit.

- (F00731) Supernet 10.239.80.0/20 is delegated to Aldermere (test) and summarised at border-4; the overlap check against Aldermere passed in review 593, and 5 exceptions are documented in IPAM ticket IPAM-9858.

- (F00732) Subnet 10.45.52.0/22 is allocated to bastion workloads in Brightholm/preprod; gateway .1, 2 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 47% at last audit.

- (F00733) Subnet 10.243.63.0/26 is allocated to data workloads in Fernhollow/test; gateway .1, 19 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 40% at last audit.

- (F00734) NAT pool 10.175.193.0/28 serves outbound traffic for reports in Eastvale, supports 43355 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00735) Supernet 10.59.128.0/18 is delegated to Brightholm (preprod) and summarised at border-1; the overlap check against Aldermere passed in review 191, and 2 exceptions are documented in IPAM ticket IPAM-4082.

- (F00736) NAT pool 10.188.65.0/28 serves outbound traffic for mailer in Aldermere, supports 25416 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00737) Subnet 10.97.198.0/26 is allocated to bastion workloads in Cresswick/prod; gateway .1, 12 addresses reserved, DHCP relay to dhcp-3, growth headroom 20% and utilisation 78% at last audit.

- (F00738) NAT pool 10.113.54.0/28 serves outbound traffic for reports in Eastvale, supports 1102 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

## Page 83: DHCP scopes [addressing]

- (F00739) Subnet 10.233.75.0/24 is allocated to queue workloads in Cresswick/preprod; gateway .1, 6 addresses reserved, DHCP relay to dhcp-1, growth headroom 25% and utilisation 51% at last audit.

- (F00740) NAT pool 10.140.244.0/28 serves outbound traffic for gateway in Fernhollow, supports 32941 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00741) Supernet 10.107.0.0/16 is delegated to Aldermere (test) and summarised at border-6; the overlap check against Fernhollow passed in review 153, and 6 exceptions are documented in IPAM ticket IPAM-3933.

- (F00742) Supernet 10.81.0.0/18 is delegated to Fernhollow (dr) and summarised at border-5; the overlap check against Dunmoor passed in review 445, and 3 exceptions are documented in IPAM ticket IPAM-8756.

- (F00743) Supernet 10.144.0.0/16 is delegated to Dunmoor (dr) and summarised at border-6; the overlap check against Brightholm passed in review 817, and 6 exceptions are documented in IPAM ticket IPAM-9978.

- (F00744) Supernet 10.27.128.0/18 is delegated to Aldermere (preprod) and summarised at border-4; the overlap check against Fernhollow passed in review 267, and 4 exceptions are documented in IPAM ticket IPAM-3253.

- (F00745) Supernet 10.74.64.0/18 is delegated to Fernhollow (dr) and summarised at border-2; the overlap check against Fernhollow passed in review 300, and 5 exceptions are documented in IPAM ticket IPAM-1149.

- (F00746) Supernet 10.75.0.0/16 is delegated to Fernhollow (mgmt) and summarised at border-4; the overlap check against Fernhollow passed in review 961, and 1 exceptions are documented in IPAM ticket IPAM-1922.

- (F00747) Subnet 10.26.60.0/22 is allocated to batch workloads in Cresswick/dr; gateway .1, 20 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 43% at last audit.

## Page 84: IPv4 supernets [addressing]

- (F00748) Subnet 10.154.88.0/24 is allocated to bastion workloads in Brightholm/dr; gateway .1, 4 addresses reserved, DHCP relay to dhcp-4, growth headroom 30% and utilisation 47% at last audit.

- (F00749) NAT pool 10.188.5.0/28 serves outbound traffic for catalogue in Fernhollow, supports 8143 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00750) Supernet 10.11.0.0/16 is delegated to Fernhollow (mgmt) and summarised at border-3; the overlap check against Fernhollow passed in review 863, and 0 exceptions are documented in IPAM ticket IPAM-3967.

- (F00751) Supernet 10.64.0.0/18 is delegated to Dunmoor (dr) and summarised at border-3; the overlap check against Aldermere passed in review 830, and 6 exceptions are documented in IPAM ticket IPAM-9806.

- (F00752) Subnet 10.250.32.0/24 is allocated to app workloads in Dunmoor/prod; gateway .1, 8 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 12% at last audit.

- (F00753) NAT pool 10.62.20.0/28 serves outbound traffic for scheduler in Dunmoor, supports 38188 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00754) Subnet 10.17.43.0/24 is allocated to app workloads in Aldermere/mgmt; gateway .1, 18 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 66% at last audit.

- (F00755) NAT pool 10.153.23.0/28 serves outbound traffic for telemetry in Aldermere, supports 43698 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00756) Subnet 10.160.180.0/26 is allocated to cache workloads in Eastvale/dr; gateway .1, 5 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 36% at last audit.

## Page 85: Site allocations [addressing]

- (F00757) Supernet 10.110.176.0/20 is delegated to Brightholm (preprod) and summarised at border-3; the overlap check against Brightholm passed in review 846, and 4 exceptions are documented in IPAM ticket IPAM-7914.

- (F00758) Subnet 10.195.83.0/24 is allocated to bastion workloads in Eastvale/test; gateway .1, 16 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 30% at last audit.

- (F00759) NAT pool 10.137.98.0/28 serves outbound traffic for mailer in Brightholm, supports 37438 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00760) NAT pool 10.214.78.0/28 serves outbound traffic for mailer in Eastvale, supports 52128 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F00761) Subnet 10.138.60.0/22 is allocated to app workloads in Eastvale/preprod; gateway .1, 19 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 23% at last audit.

- (F00762) Supernet 10.115.0.0/16 is delegated to Cresswick (test) and summarised at border-1; the overlap check against Aldermere passed in review 486, and 1 exceptions are documented in IPAM ticket IPAM-7203.

- (F00763) Subnet 10.156.250.0/26 is allocated to app workloads in Aldermere/preprod; gateway .1, 18 addresses reserved, DHCP relay to dhcp-3, growth headroom 25% and utilisation 82% at last audit.

- (F00764) Supernet 10.87.0.0/16 is delegated to Eastvale (prod) and summarised at border-4; the overlap check against Brightholm passed in review 453, and 6 exceptions are documented in IPAM ticket IPAM-9711.

- (F00765) NAT pool 10.244.65.0/28 serves outbound traffic for telemetry in Eastvale, supports 1122 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

## Page 86: Site allocations [addressing]

- (F00766) NAT pool 10.193.136.0/28 serves outbound traffic for ledger in Brightholm, supports 48041 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00767) NAT pool 10.214.234.0/28 serves outbound traffic for scheduler in Brightholm, supports 29267 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F00768) NAT pool 10.219.117.0/28 serves outbound traffic for telemetry in Cresswick, supports 42156 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F00769) Supernet 10.40.32.0/20 is delegated to Cresswick (prod) and summarised at border-6; the overlap check against Brightholm passed in review 195, and 1 exceptions are documented in IPAM ticket IPAM-1940.

- (F00770) Subnet 10.252.5.0/26 is allocated to bastion workloads in Fernhollow/test; gateway .1, 18 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 77% at last audit.

- (F00771) NAT pool 10.63.207.0/28 serves outbound traffic for ledger in Fernhollow, supports 40888 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00772) Subnet 10.176.125.0/26 is allocated to web workloads in Fernhollow/dr; gateway .1, 16 addresses reserved, DHCP relay to dhcp-2, growth headroom 20% and utilisation 34% at last audit.

- (F00773) Subnet 10.180.26.0/26 is allocated to bastion workloads in Cresswick/preprod; gateway .1, 17 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 26% at last audit.

- (F00774) Supernet 10.60.144.0/20 is delegated to Fernhollow (preprod) and summarised at border-3; the overlap check against Dunmoor passed in review 400, and 2 exceptions are documented in IPAM ticket IPAM-4490.

## Page 87: IPv4 supernets [addressing]

- (F00775) NAT pool 10.201.111.0/28 serves outbound traffic for telemetry in Fernhollow, supports 42637 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00776) Supernet 10.182.0.0/16 is delegated to Eastvale (dr) and summarised at border-5; the overlap check against Dunmoor passed in review 436, and 2 exceptions are documented in IPAM ticket IPAM-6798.

- (F00777) Subnet 10.95.205.0/26 is allocated to batch workloads in Aldermere/test; gateway .1, 2 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 37% at last audit.

- (F00778) Subnet 10.210.60.0/22 is allocated to monitoring workloads in Eastvale/mgmt; gateway .1, 2 addresses reserved, DHCP relay to dhcp-2, growth headroom 25% and utilisation 40% at last audit.

- (F00779) Supernet 10.186.192.0/18 is delegated to Dunmoor (test) and summarised at border-2; the overlap check against Eastvale passed in review 931, and 2 exceptions are documented in IPAM ticket IPAM-2780.

- (F00780) Supernet 10.71.0.0/16 is delegated to Fernhollow (dr) and summarised at border-6; the overlap check against Dunmoor passed in review 105, and 2 exceptions are documented in IPAM ticket IPAM-4251.

- (F00781) Subnet 10.68.200.0/22 is allocated to bastion workloads in Brightholm/test; gateway .1, 12 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 73% at last audit.

- (F00782) NAT pool 10.215.250.0/28 serves outbound traffic for identity in Cresswick, supports 52917 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00783) Subnet 10.199.67.0/26 is allocated to app workloads in Cresswick/dr; gateway .1, 5 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 56% at last audit.

## Page 88: NAT pools [addressing]

- (F00784) Subnet 10.175.216.0/22 is allocated to web workloads in Fernhollow/preprod; gateway .1, 15 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 74% at last audit.

- (F00785) Subnet 10.78.95.0/26 is allocated to cache workloads in Dunmoor/preprod; gateway .1, 10 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 66% at last audit.

- (F00786) Subnet 10.92.96.0/26 is allocated to data workloads in Dunmoor/prod; gateway .1, 9 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 16% at last audit.

- (F00787) Supernet 10.9.64.0/18 is delegated to Brightholm (preprod) and summarised at border-1; the overlap check against Aldermere passed in review 489, and 3 exceptions are documented in IPAM ticket IPAM-9601.

- (F00788) Supernet 10.172.0.0/16 is delegated to Fernhollow (preprod) and summarised at border-4; the overlap check against Aldermere passed in review 622, and 3 exceptions are documented in IPAM ticket IPAM-1846.

- (F00789) Supernet 10.143.128.0/18 is delegated to Aldermere (test) and summarised at border-6; the overlap check against Dunmoor passed in review 352, and 2 exceptions are documented in IPAM ticket IPAM-1779.

- (F00790) Subnet 10.164.108.0/22 is allocated to queue workloads in Aldermere/prod; gateway .1, 17 addresses reserved, DHCP relay to dhcp-3, growth headroom 15% and utilisation 67% at last audit.

- (F00791) Subnet 10.171.155.0/24 is allocated to app workloads in Cresswick/dr; gateway .1, 5 addresses reserved, DHCP relay to dhcp-1, growth headroom 20% and utilisation 54% at last audit.

- (F00792) Supernet 10.190.112.0/20 is delegated to Fernhollow (test) and summarised at border-6; the overlap check against Cresswick passed in review 315, and 4 exceptions are documented in IPAM ticket IPAM-7292.

## Page 89: IPv4 supernets [addressing]

- (F00793) Subnet 10.21.96.0/22 is allocated to cache workloads in Brightholm/mgmt; gateway .1, 16 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 50% at last audit.

- (F00794) NAT pool 10.78.22.0/28 serves outbound traffic for scheduler in Dunmoor, supports 13063 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00795) NAT pool 10.177.187.0/28 serves outbound traffic for identity in Cresswick, supports 41778 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00796) Supernet 10.11.64.0/18 is delegated to Aldermere (dr) and summarised at border-5; the overlap check against Cresswick passed in review 813, and 1 exceptions are documented in IPAM ticket IPAM-5745.

- (F00797) Subnet 10.97.203.0/26 is allocated to monitoring workloads in Eastvale/prod; gateway .1, 19 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 77% at last audit.

- (F00798) Supernet 10.139.64.0/18 is delegated to Eastvale (dr) and summarised at border-2; the overlap check against Aldermere passed in review 263, and 4 exceptions are documented in IPAM ticket IPAM-4568.

- (F00799) NAT pool 10.233.132.0/28 serves outbound traffic for telemetry in Fernhollow, supports 56367 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F00800) NAT pool 10.60.87.0/28 serves outbound traffic for gateway in Cresswick, supports 3489 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00801) Supernet 10.68.128.0/18 is delegated to Aldermere (preprod) and summarised at border-1; the overlap check against Fernhollow passed in review 354, and 6 exceptions are documented in IPAM ticket IPAM-4440.

## Page 90: NAT pools [addressing]

- (F00802) Subnet 10.188.166.0/26 is allocated to app workloads in Aldermere/test; gateway .1, 19 addresses reserved, DHCP relay to dhcp-3, growth headroom 20% and utilisation 64% at last audit.

- (F00803) NAT pool 10.29.5.0/28 serves outbound traffic for mailer in Cresswick, supports 14870 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00804) Subnet 10.54.195.0/26 is allocated to queue workloads in Cresswick/prod; gateway .1, 19 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 53% at last audit.

- (F00805) Supernet 10.202.64.0/20 is delegated to Brightholm (mgmt) and summarised at border-4; the overlap check against Brightholm passed in review 847, and 5 exceptions are documented in IPAM ticket IPAM-8109.

- (F00806) Supernet 10.253.0.0/16 is delegated to Brightholm (dr) and summarised at border-4; the overlap check against Brightholm passed in review 935, and 6 exceptions are documented in IPAM ticket IPAM-3885.

- (F00807) Subnet 10.92.144.0/26 is allocated to web workloads in Eastvale/dr; gateway .1, 11 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 36% at last audit.

- (F00808) Subnet 10.125.232.0/24 is allocated to bastion workloads in Brightholm/prod; gateway .1, 5 addresses reserved, DHCP relay to dhcp-2, growth headroom 15% and utilisation 24% at last audit.

- (F00809) Supernet 10.6.0.0/16 is delegated to Dunmoor (prod) and summarised at border-2; the overlap check against Brightholm passed in review 888, and 0 exceptions are documented in IPAM ticket IPAM-5385.

- (F00810) Subnet 10.4.52.0/22 is allocated to batch workloads in Fernhollow/mgmt; gateway .1, 4 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 84% at last audit.

## Page 91: Management ranges [addressing]

- (F00811) Subnet 10.79.124.0/24 is allocated to web workloads in Cresswick/test; gateway .1, 19 addresses reserved, DHCP relay to dhcp-3, growth headroom 15% and utilisation 14% at last audit.

- (F00812) Subnet 10.52.212.0/24 is allocated to data workloads in Aldermere/mgmt; gateway .1, 2 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 66% at last audit.

- (F00813) Supernet 10.146.112.0/20 is delegated to Brightholm (test) and summarised at border-6; the overlap check against Dunmoor passed in review 803, and 5 exceptions are documented in IPAM ticket IPAM-2841.

- (F00814) Supernet 10.52.0.0/16 is delegated to Brightholm (prod) and summarised at border-3; the overlap check against Aldermere passed in review 730, and 2 exceptions are documented in IPAM ticket IPAM-2939.

- (F00815) Supernet 10.77.80.0/20 is delegated to Aldermere (prod) and summarised at border-4; the overlap check against Eastvale passed in review 442, and 4 exceptions are documented in IPAM ticket IPAM-3971.

- (F00816) NAT pool 10.154.146.0/28 serves outbound traffic for mailer in Dunmoor, supports 57870 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F00817) Supernet 10.39.0.0/18 is delegated to Fernhollow (test) and summarised at border-2; the overlap check against Fernhollow passed in review 250, and 2 exceptions are documented in IPAM ticket IPAM-3421.

- (F00818) Supernet 10.57.0.0/16 is delegated to Dunmoor (dr) and summarised at border-6; the overlap check against Cresswick passed in review 248, and 0 exceptions are documented in IPAM ticket IPAM-6292.

- (F00819) Subnet 10.163.253.0/24 is allocated to bastion workloads in Brightholm/dr; gateway .1, 17 addresses reserved, DHCP relay to dhcp-4, growth headroom 25% and utilisation 29% at last audit.

## Page 92: Site allocations [addressing]

- (F00820) Supernet 10.252.64.0/18 is delegated to Dunmoor (mgmt) and summarised at border-4; the overlap check against Aldermere passed in review 694, and 5 exceptions are documented in IPAM ticket IPAM-7911.

- (F00821) NAT pool 10.44.120.0/28 serves outbound traffic for mailer in Eastvale, supports 687 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00822) Supernet 10.56.0.0/16 is delegated to Eastvale (dr) and summarised at border-3; the overlap check against Cresswick passed in review 969, and 6 exceptions are documented in IPAM ticket IPAM-3283.

- (F00823) Supernet 10.215.112.0/20 is delegated to Dunmoor (preprod) and summarised at border-2; the overlap check against Brightholm passed in review 157, and 5 exceptions are documented in IPAM ticket IPAM-3257.

- (F00824) Subnet 10.13.217.0/24 is allocated to batch workloads in Fernhollow/preprod; gateway .1, 3 addresses reserved, DHCP relay to dhcp-1, growth headroom 15% and utilisation 73% at last audit.

- (F00825) NAT pool 10.75.187.0/28 serves outbound traffic for scheduler in Brightholm, supports 5676 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00826) Subnet 10.93.240.0/22 is allocated to data workloads in Eastvale/dr; gateway .1, 18 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 55% at last audit.

- (F00827) Supernet 10.56.64.0/18 is delegated to Fernhollow (prod) and summarised at border-1; the overlap check against Fernhollow passed in review 132, and 4 exceptions are documented in IPAM ticket IPAM-3843.

- (F00828) NAT pool 10.202.216.0/28 serves outbound traffic for identity in Brightholm, supports 36817 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

## Page 93: NAT pools [addressing]

- (F00829) NAT pool 10.216.80.0/28 serves outbound traffic for telemetry in Cresswick, supports 6525 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00830) Subnet 10.28.112.0/24 is allocated to bastion workloads in Fernhollow/preprod; gateway .1, 7 addresses reserved, DHCP relay to dhcp-1, growth headroom 30% and utilisation 73% at last audit.

- (F00831) Supernet 10.84.0.0/18 is delegated to Fernhollow (dr) and summarised at border-3; the overlap check against Fernhollow passed in review 534, and 1 exceptions are documented in IPAM ticket IPAM-5422.

- (F00832) Subnet 10.171.14.0/24 is allocated to cache workloads in Aldermere/prod; gateway .1, 11 addresses reserved, DHCP relay to dhcp-2, growth headroom 15% and utilisation 20% at last audit.

- (F00833) Subnet 10.96.103.0/24 is allocated to web workloads in Eastvale/prod; gateway .1, 9 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 84% at last audit.

- (F00834) Supernet 10.47.128.0/18 is delegated to Aldermere (prod) and summarised at border-1; the overlap check against Cresswick passed in review 869, and 2 exceptions are documented in IPAM ticket IPAM-7523.

- (F00835) NAT pool 10.200.182.0/28 serves outbound traffic for scheduler in Brightholm, supports 46549 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00836) Supernet 10.76.0.0/16 is delegated to Dunmoor (mgmt) and summarised at border-5; the overlap check against Dunmoor passed in review 588, and 4 exceptions are documented in IPAM ticket IPAM-1612.

- (F00837) Supernet 10.237.32.0/20 is delegated to Brightholm (preprod) and summarised at border-6; the overlap check against Aldermere passed in review 835, and 1 exceptions are documented in IPAM ticket IPAM-4533.

## Page 94: Site allocations [addressing]

- (F00838) NAT pool 10.174.229.0/28 serves outbound traffic for scheduler in Brightholm, supports 22718 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F00839) NAT pool 10.198.122.0/28 serves outbound traffic for gateway in Dunmoor, supports 40502 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00840) Subnet 10.7.72.0/22 is allocated to queue workloads in Eastvale/dr; gateway .1, 19 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 70% at last audit.

- (F00841) Supernet 10.34.0.0/16 is delegated to Brightholm (test) and summarised at border-5; the overlap check against Cresswick passed in review 461, and 0 exceptions are documented in IPAM ticket IPAM-2165.

- (F00842) Subnet 10.242.131.0/24 is allocated to monitoring workloads in Fernhollow/dr; gateway .1, 6 addresses reserved, DHCP relay to dhcp-1, growth headroom 30% and utilisation 17% at last audit.

- (F00843) Supernet 10.66.192.0/18 is delegated to Cresswick (dr) and summarised at border-3; the overlap check against Eastvale passed in review 965, and 4 exceptions are documented in IPAM ticket IPAM-6138.

- (F00844) Supernet 10.230.128.0/20 is delegated to Aldermere (dr) and summarised at border-6; the overlap check against Aldermere passed in review 735, and 5 exceptions are documented in IPAM ticket IPAM-1934.

- (F00845) NAT pool 10.4.79.0/28 serves outbound traffic for catalogue in Brightholm, supports 19548 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00846) NAT pool 10.114.198.0/28 serves outbound traffic for identity in Dunmoor, supports 44353 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

## Page 95: Management ranges [addressing]

- (F00847) Supernet 10.55.0.0/18 is delegated to Fernhollow (mgmt) and summarised at border-2; the overlap check against Fernhollow passed in review 210, and 3 exceptions are documented in IPAM ticket IPAM-8096.

- (F00848) Subnet 10.162.172.0/22 is allocated to monitoring workloads in Dunmoor/test; gateway .1, 8 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 70% at last audit.

- (F00849) Subnet 10.74.109.0/24 is allocated to batch workloads in Eastvale/preprod; gateway .1, 20 addresses reserved, DHCP relay to dhcp-1, growth headroom 30% and utilisation 19% at last audit.

- (F00850) Supernet 10.27.0.0/16 is delegated to Dunmoor (dr) and summarised at border-1; the overlap check against Fernhollow passed in review 533, and 2 exceptions are documented in IPAM ticket IPAM-5129.

- (F00851) NAT pool 10.72.35.0/28 serves outbound traffic for telemetry in Brightholm, supports 27046 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F00852) NAT pool 10.109.132.0/28 serves outbound traffic for scheduler in Dunmoor, supports 54930 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00853) Supernet 10.101.0.0/16 is delegated to Cresswick (test) and summarised at border-4; the overlap check against Dunmoor passed in review 586, and 4 exceptions are documented in IPAM ticket IPAM-3632.

- (F00854) NAT pool 10.199.5.0/28 serves outbound traffic for gateway in Dunmoor, supports 5599 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00855) NAT pool 10.165.162.0/28 serves outbound traffic for ledger in Eastvale, supports 10363 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

## Page 96: Management ranges [addressing]

- (F00856) Supernet 10.1.192.0/18 is delegated to Aldermere (dr) and summarised at border-2; the overlap check against Fernhollow passed in review 560, and 5 exceptions are documented in IPAM ticket IPAM-2596.

- (F00857) Subnet 10.85.193.0/24 is allocated to cache workloads in Brightholm/preprod; gateway .1, 13 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 59% at last audit.

- (F00858) Supernet 10.63.192.0/18 is delegated to Aldermere (test) and summarised at border-6; the overlap check against Dunmoor passed in review 523, and 3 exceptions are documented in IPAM ticket IPAM-6762.

- (F00859) Supernet 10.171.48.0/20 is delegated to Eastvale (dr) and summarised at border-2; the overlap check against Dunmoor passed in review 538, and 2 exceptions are documented in IPAM ticket IPAM-3898.

- (F00860) NAT pool 10.223.195.0/28 serves outbound traffic for telemetry in Eastvale, supports 55883 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00861) NAT pool 10.50.44.0/28 serves outbound traffic for catalogue in Dunmoor, supports 6374 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00862) NAT pool 10.254.51.0/28 serves outbound traffic for identity in Dunmoor, supports 33488 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00863) NAT pool 10.108.114.0/28 serves outbound traffic for identity in Cresswick, supports 36648 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00864) Subnet 10.237.211.0/24 is allocated to bastion workloads in Dunmoor/prod; gateway .1, 2 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 46% at last audit.

## Page 97: DHCP scopes [addressing]

- (F00865) Supernet 10.212.0.0/16 is delegated to Dunmoor (preprod) and summarised at border-1; the overlap check against Aldermere passed in review 257, and 6 exceptions are documented in IPAM ticket IPAM-7134.

- (F00866) NAT pool 10.162.171.0/28 serves outbound traffic for scheduler in Fernhollow, supports 37998 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00867) NAT pool 10.201.26.0/28 serves outbound traffic for reports in Dunmoor, supports 8945 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00868) NAT pool 10.162.81.0/28 serves outbound traffic for reports in Brightholm, supports 15636 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00869) Subnet 10.200.133.0/26 is allocated to data workloads in Eastvale/prod; gateway .1, 12 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 15% at last audit.

- (F00870) Supernet 10.14.0.0/16 is delegated to Aldermere (mgmt) and summarised at border-5; the overlap check against Dunmoor passed in review 125, and 5 exceptions are documented in IPAM ticket IPAM-3138.

- (F00871) Supernet 10.122.0.0/16 is delegated to Fernhollow (test) and summarised at border-3; the overlap check against Brightholm passed in review 648, and 6 exceptions are documented in IPAM ticket IPAM-5018.

- (F00872) NAT pool 10.26.140.0/28 serves outbound traffic for catalogue in Dunmoor, supports 9922 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00873) NAT pool 10.56.235.0/28 serves outbound traffic for catalogue in Eastvale, supports 7517 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

## Page 98: DHCP scopes [addressing]

- (F00874) Subnet 10.185.106.0/24 is allocated to bastion workloads in Aldermere/prod; gateway .1, 5 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 21% at last audit.

- (F00875) Supernet 10.214.0.0/16 is delegated to Fernhollow (prod) and summarised at border-3; the overlap check against Fernhollow passed in review 561, and 6 exceptions are documented in IPAM ticket IPAM-3639.

- (F00876) Subnet 10.16.60.0/22 is allocated to batch workloads in Cresswick/prod; gateway .1, 13 addresses reserved, DHCP relay to dhcp-4, growth headroom 15% and utilisation 32% at last audit.

- (F00877) NAT pool 10.62.98.0/28 serves outbound traffic for ledger in Fernhollow, supports 35624 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00878) NAT pool 10.186.58.0/28 serves outbound traffic for gateway in Brightholm, supports 2433 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00879) Subnet 10.140.246.0/24 is allocated to cache workloads in Aldermere/preprod; gateway .1, 4 addresses reserved, DHCP relay to dhcp-3, growth headroom 25% and utilisation 71% at last audit.

- (F00880) NAT pool 10.204.98.0/28 serves outbound traffic for telemetry in Dunmoor, supports 11835 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00881) NAT pool 10.52.159.0/28 serves outbound traffic for scheduler in Cresswick, supports 52542 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00882) Supernet 10.139.128.0/18 is delegated to Dunmoor (dr) and summarised at border-5; the overlap check against Aldermere passed in review 721, and 3 exceptions are documented in IPAM ticket IPAM-8033.

## Page 99: Site allocations [addressing]

- (F00883) NAT pool 10.32.230.0/28 serves outbound traffic for scheduler in Cresswick, supports 58790 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00884) Supernet 10.180.192.0/18 is delegated to Eastvale (dr) and summarised at border-1; the overlap check against Aldermere passed in review 284, and 6 exceptions are documented in IPAM ticket IPAM-6286.

- (F00885) Supernet 10.37.0.0/16 is delegated to Brightholm (test) and summarised at border-6; the overlap check against Cresswick passed in review 480, and 1 exceptions are documented in IPAM ticket IPAM-6151.

- (F00886) Subnet 10.5.168.0/26 is allocated to cache workloads in Aldermere/test; gateway .1, 16 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 61% at last audit.

- (F00887) Supernet 10.111.48.0/20 is delegated to Eastvale (preprod) and summarised at border-5; the overlap check against Cresswick passed in review 833, and 4 exceptions are documented in IPAM ticket IPAM-2225.

- (F00888) NAT pool 10.222.162.0/28 serves outbound traffic for mailer in Fernhollow, supports 13485 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00889) Supernet 10.215.0.0/18 is delegated to Dunmoor (prod) and summarised at border-1; the overlap check against Dunmoor passed in review 275, and 4 exceptions are documented in IPAM ticket IPAM-6355.

- (F00890) NAT pool 10.10.145.0/28 serves outbound traffic for ledger in Dunmoor, supports 42683 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00891) Supernet 10.18.0.0/18 is delegated to Cresswick (preprod) and summarised at border-3; the overlap check against Fernhollow passed in review 116, and 0 exceptions are documented in IPAM ticket IPAM-8698.

## Page 100: IPv4 supernets [addressing]

- (F00892) Supernet 10.162.128.0/18 is delegated to Fernhollow (test) and summarised at border-4; the overlap check against Aldermere passed in review 669, and 6 exceptions are documented in IPAM ticket IPAM-6131.

- (F00893) Supernet 10.152.192.0/18 is delegated to Eastvale (prod) and summarised at border-4; the overlap check against Fernhollow passed in review 224, and 6 exceptions are documented in IPAM ticket IPAM-7126.

- (F00894) NAT pool 10.114.24.0/28 serves outbound traffic for ledger in Aldermere, supports 9592 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F00895) NAT pool 10.115.87.0/28 serves outbound traffic for catalogue in Fernhollow, supports 13027 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00896) NAT pool 10.132.22.0/28 serves outbound traffic for catalogue in Aldermere, supports 3645 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00897) Supernet 10.138.64.0/18 is delegated to Cresswick (mgmt) and summarised at border-2; the overlap check against Eastvale passed in review 571, and 0 exceptions are documented in IPAM ticket IPAM-3069.

- (F00898) Supernet 10.228.0.0/18 is delegated to Brightholm (mgmt) and summarised at border-5; the overlap check against Eastvale passed in review 346, and 4 exceptions are documented in IPAM ticket IPAM-8830.

- (F00899) NAT pool 10.164.247.0/28 serves outbound traffic for gateway in Dunmoor, supports 6516 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F00900) NAT pool 10.124.105.0/28 serves outbound traffic for catalogue in Aldermere, supports 5424 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

## Page 101: Site allocations [addressing]

- (F00901) Subnet 10.197.96.0/24 is allocated to monitoring workloads in Fernhollow/preprod; gateway .1, 5 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 51% at last audit.

- (F00902) NAT pool 10.54.66.0/28 serves outbound traffic for gateway in Dunmoor, supports 24331 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F00903) NAT pool 10.204.96.0/28 serves outbound traffic for catalogue in Eastvale, supports 18708 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00904) NAT pool 10.52.75.0/28 serves outbound traffic for identity in Cresswick, supports 57922 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00905) Subnet 10.95.136.0/24 is allocated to web workloads in Brightholm/prod; gateway .1, 17 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 27% at last audit.

- (F00906) NAT pool 10.220.108.0/28 serves outbound traffic for scheduler in Aldermere, supports 26513 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00907) NAT pool 10.225.139.0/28 serves outbound traffic for mailer in Cresswick, supports 6910 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00908) Supernet 10.150.0.0/16 is delegated to Fernhollow (dr) and summarised at border-4; the overlap check against Brightholm passed in review 708, and 2 exceptions are documented in IPAM ticket IPAM-9676.

- (F00909) NAT pool 10.221.55.0/28 serves outbound traffic for ledger in Dunmoor, supports 42858 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

## Page 102: Site allocations [addressing]

- (F00910) Subnet 10.136.122.0/26 is allocated to app workloads in Aldermere/prod; gateway .1, 19 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 63% at last audit.

- (F00911) Supernet 10.137.0.0/16 is delegated to Dunmoor (prod) and summarised at border-2; the overlap check against Brightholm passed in review 904, and 1 exceptions are documented in IPAM ticket IPAM-6695.

- (F00912) NAT pool 10.147.1.0/28 serves outbound traffic for catalogue in Cresswick, supports 12629 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00913) NAT pool 10.122.87.0/28 serves outbound traffic for mailer in Dunmoor, supports 45159 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00914) Subnet 10.6.240.0/22 is allocated to bastion workloads in Cresswick/dr; gateway .1, 12 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 21% at last audit.

- (F00915) Subnet 10.180.242.0/26 is allocated to web workloads in Fernhollow/prod; gateway .1, 17 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 17% at last audit.

- (F00916) Subnet 10.85.72.0/22 is allocated to app workloads in Eastvale/test; gateway .1, 5 addresses reserved, DHCP relay to dhcp-3, growth headroom 25% and utilisation 69% at last audit.

- (F00917) Supernet 10.131.240.0/20 is delegated to Fernhollow (test) and summarised at border-3; the overlap check against Cresswick passed in review 569, and 0 exceptions are documented in IPAM ticket IPAM-6777.

- (F00918) Supernet 10.247.48.0/20 is delegated to Fernhollow (test) and summarised at border-3; the overlap check against Fernhollow passed in review 631, and 5 exceptions are documented in IPAM ticket IPAM-1339.

## Page 103: Site allocations [addressing]

- (F00919) Supernet 10.254.0.0/18 is delegated to Brightholm (preprod) and summarised at border-2; the overlap check against Eastvale passed in review 858, and 5 exceptions are documented in IPAM ticket IPAM-8056.

- (F00920) Supernet 10.193.0.0/16 is delegated to Brightholm (prod) and summarised at border-3; the overlap check against Fernhollow passed in review 795, and 4 exceptions are documented in IPAM ticket IPAM-8360.

- (F00921) NAT pool 10.178.169.0/28 serves outbound traffic for reports in Brightholm, supports 39110 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F00922) Supernet 10.175.48.0/20 is delegated to Brightholm (prod) and summarised at border-4; the overlap check against Dunmoor passed in review 680, and 6 exceptions are documented in IPAM ticket IPAM-6685.

- (F00923) Supernet 10.75.192.0/18 is delegated to Aldermere (prod) and summarised at border-6; the overlap check against Brightholm passed in review 635, and 2 exceptions are documented in IPAM ticket IPAM-3664.

- (F00924) Supernet 10.150.0.0/16 is delegated to Dunmoor (test) and summarised at border-4; the overlap check against Aldermere passed in review 322, and 2 exceptions are documented in IPAM ticket IPAM-3022.

- (F00925) Subnet 10.220.180.0/22 is allocated to web workloads in Dunmoor/test; gateway .1, 3 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 48% at last audit.

- (F00926) NAT pool 10.79.44.0/28 serves outbound traffic for telemetry in Fernhollow, supports 9848 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00927) Supernet 10.112.0.0/18 is delegated to Eastvale (prod) and summarised at border-4; the overlap check against Cresswick passed in review 354, and 6 exceptions are documented in IPAM ticket IPAM-7328.

## Page 104: Management ranges [addressing]

- (F00928) Supernet 10.159.64.0/18 is delegated to Aldermere (test) and summarised at border-5; the overlap check against Dunmoor passed in review 795, and 2 exceptions are documented in IPAM ticket IPAM-3280.

- (F00929) NAT pool 10.69.213.0/28 serves outbound traffic for gateway in Brightholm, supports 20230 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00930) Supernet 10.93.192.0/20 is delegated to Eastvale (dr) and summarised at border-4; the overlap check against Aldermere passed in review 241, and 4 exceptions are documented in IPAM ticket IPAM-8240.

- (F00931) NAT pool 10.183.239.0/28 serves outbound traffic for mailer in Cresswick, supports 28527 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F00932) Supernet 10.13.208.0/20 is delegated to Dunmoor (prod) and summarised at border-1; the overlap check against Brightholm passed in review 729, and 2 exceptions are documented in IPAM ticket IPAM-4975.

- (F00933) NAT pool 10.65.150.0/28 serves outbound traffic for ledger in Eastvale, supports 50001 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00934) Supernet 10.235.0.0/18 is delegated to Fernhollow (prod) and summarised at border-1; the overlap check against Aldermere passed in review 376, and 6 exceptions are documented in IPAM ticket IPAM-2753.

- (F00935) Supernet 10.246.128.0/18 is delegated to Eastvale (prod) and summarised at border-1; the overlap check against Aldermere passed in review 858, and 4 exceptions are documented in IPAM ticket IPAM-9369.

- (F00936) NAT pool 10.104.73.0/28 serves outbound traffic for identity in Fernhollow, supports 9439 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

## Page 105: Site allocations [addressing]

- (F00937) Supernet 10.3.240.0/20 is delegated to Fernhollow (test) and summarised at border-5; the overlap check against Fernhollow passed in review 305, and 0 exceptions are documented in IPAM ticket IPAM-2100.

- (F00938) Subnet 10.49.124.0/22 is allocated to cache workloads in Brightholm/mgmt; gateway .1, 5 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 62% at last audit.

- (F00939) Subnet 10.247.94.0/24 is allocated to cache workloads in Aldermere/test; gateway .1, 19 addresses reserved, DHCP relay to dhcp-3, growth headroom 30% and utilisation 27% at last audit.

- (F00940) Supernet 10.72.0.0/16 is delegated to Brightholm (prod) and summarised at border-2; the overlap check against Eastvale passed in review 859, and 5 exceptions are documented in IPAM ticket IPAM-9956.

- (F00941) Subnet 10.148.51.0/24 is allocated to monitoring workloads in Dunmoor/dr; gateway .1, 13 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 25% at last audit.

- (F00942) Supernet 10.14.0.0/16 is delegated to Dunmoor (dr) and summarised at border-4; the overlap check against Aldermere passed in review 677, and 3 exceptions are documented in IPAM ticket IPAM-1180.

- (F00943) NAT pool 10.227.21.0/28 serves outbound traffic for mailer in Cresswick, supports 9629 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00944) Supernet 10.183.0.0/16 is delegated to Cresswick (prod) and summarised at border-3; the overlap check against Fernhollow passed in review 637, and 3 exceptions are documented in IPAM ticket IPAM-9405.

- (F00945) Subnet 10.173.235.0/24 is allocated to data workloads in Brightholm/preprod; gateway .1, 10 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 73% at last audit.

## Page 106: Management ranges [addressing]

- (F00946) Supernet 10.132.64.0/20 is delegated to Eastvale (preprod) and summarised at border-6; the overlap check against Cresswick passed in review 702, and 4 exceptions are documented in IPAM ticket IPAM-6703.

- (F00947) NAT pool 10.34.23.0/28 serves outbound traffic for ledger in Eastvale, supports 56338 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00948) Subnet 10.243.165.0/24 is allocated to cache workloads in Aldermere/prod; gateway .1, 9 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 65% at last audit.

- (F00949) Subnet 10.58.19.0/24 is allocated to app workloads in Aldermere/mgmt; gateway .1, 16 addresses reserved, DHCP relay to dhcp-3, growth headroom 15% and utilisation 34% at last audit.

- (F00950) Supernet 10.68.64.0/18 is delegated to Aldermere (dr) and summarised at border-2; the overlap check against Cresswick passed in review 602, and 3 exceptions are documented in IPAM ticket IPAM-5687.

- (F00951) Subnet 10.98.44.0/24 is allocated to web workloads in Brightholm/preprod; gateway .1, 5 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 12% at last audit.

- (F00952) Supernet 10.36.160.0/20 is delegated to Dunmoor (mgmt) and summarised at border-2; the overlap check against Fernhollow passed in review 847, and 5 exceptions are documented in IPAM ticket IPAM-9653.

- (F00953) Supernet 10.242.176.0/20 is delegated to Brightholm (preprod) and summarised at border-3; the overlap check against Eastvale passed in review 672, and 6 exceptions are documented in IPAM ticket IPAM-3258.

- (F00954) Subnet 10.192.36.0/26 is allocated to app workloads in Dunmoor/dr; gateway .1, 6 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 75% at last audit.

## Page 107: Site allocations [addressing]

- (F00955) Subnet 10.11.114.0/24 is allocated to queue workloads in Eastvale/mgmt; gateway .1, 10 addresses reserved, DHCP relay to dhcp-4, growth headroom 25% and utilisation 20% at last audit.

- (F00956) Subnet 10.123.159.0/26 is allocated to bastion workloads in Cresswick/prod; gateway .1, 3 addresses reserved, DHCP relay to dhcp-1, growth headroom 30% and utilisation 45% at last audit.

- (F00957) NAT pool 10.173.215.0/28 serves outbound traffic for telemetry in Aldermere, supports 13640 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F00958) Subnet 10.168.31.0/26 is allocated to cache workloads in Brightholm/mgmt; gateway .1, 17 addresses reserved, DHCP relay to dhcp-1, growth headroom 15% and utilisation 56% at last audit.

- (F00959) Subnet 10.41.245.0/26 is allocated to data workloads in Dunmoor/mgmt; gateway .1, 10 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 75% at last audit.

- (F00960) NAT pool 10.220.244.0/28 serves outbound traffic for telemetry in Brightholm, supports 51719 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00961) Subnet 10.194.9.0/26 is allocated to monitoring workloads in Aldermere/preprod; gateway .1, 3 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 67% at last audit.

- (F00962) NAT pool 10.70.59.0/28 serves outbound traffic for identity in Dunmoor, supports 8232 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00963) Supernet 10.29.64.0/18 is delegated to Brightholm (test) and summarised at border-2; the overlap check against Aldermere passed in review 702, and 0 exceptions are documented in IPAM ticket IPAM-4721.

## Page 108: Management ranges [addressing]

- (F00964) NAT pool 10.23.7.0/28 serves outbound traffic for gateway in Eastvale, supports 53755 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00965) Subnet 10.144.20.0/22 is allocated to batch workloads in Brightholm/dr; gateway .1, 13 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 62% at last audit.

- (F00966) Supernet 10.39.32.0/20 is delegated to Fernhollow (prod) and summarised at border-3; the overlap check against Eastvale passed in review 310, and 3 exceptions are documented in IPAM ticket IPAM-6848.

- (F00967) Subnet 10.149.125.0/24 is allocated to queue workloads in Dunmoor/test; gateway .1, 12 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 64% at last audit.

- (F00968) NAT pool 10.143.40.0/28 serves outbound traffic for gateway in Eastvale, supports 9487 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00969) Supernet 10.62.0.0/16 is delegated to Fernhollow (mgmt) and summarised at border-6; the overlap check against Brightholm passed in review 136, and 1 exceptions are documented in IPAM ticket IPAM-8213.

- (F00970) NAT pool 10.10.255.0/28 serves outbound traffic for ledger in Dunmoor, supports 18214 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00971) Supernet 10.142.0.0/16 is delegated to Cresswick (prod) and summarised at border-4; the overlap check against Aldermere passed in review 983, and 3 exceptions are documented in IPAM ticket IPAM-7302.

- (F00972) Supernet 10.194.0.0/16 is delegated to Aldermere (preprod) and summarised at border-6; the overlap check against Dunmoor passed in review 645, and 0 exceptions are documented in IPAM ticket IPAM-5999.

## Page 109: IPv4 supernets [addressing]

- (F00973) NAT pool 10.172.134.0/28 serves outbound traffic for gateway in Cresswick, supports 50127 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F00974) NAT pool 10.218.29.0/28 serves outbound traffic for catalogue in Eastvale, supports 36760 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00975) NAT pool 10.237.217.0/28 serves outbound traffic for telemetry in Cresswick, supports 11152 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F00976) NAT pool 10.7.143.0/28 serves outbound traffic for telemetry in Brightholm, supports 6105 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00977) Supernet 10.19.128.0/18 is delegated to Cresswick (mgmt) and summarised at border-3; the overlap check against Cresswick passed in review 775, and 2 exceptions are documented in IPAM ticket IPAM-1202.

- (F00978) Subnet 10.164.135.0/26 is allocated to data workloads in Cresswick/mgmt; gateway .1, 16 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 13% at last audit.

- (F00979) Supernet 10.111.192.0/18 is delegated to Aldermere (test) and summarised at border-1; the overlap check against Eastvale passed in review 181, and 2 exceptions are documented in IPAM ticket IPAM-6145.

- (F00980) Subnet 10.141.132.0/24 is allocated to monitoring workloads in Dunmoor/preprod; gateway .1, 6 addresses reserved, DHCP relay to dhcp-2, growth headroom 20% and utilisation 30% at last audit.

- (F00981) NAT pool 10.119.58.0/28 serves outbound traffic for ledger in Fernhollow, supports 12575 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

## Page 110: Management ranges [addressing]

- (F00982) NAT pool 10.116.31.0/28 serves outbound traffic for telemetry in Cresswick, supports 17371 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F00983) Supernet 10.120.176.0/20 is delegated to Eastvale (prod) and summarised at border-1; the overlap check against Aldermere passed in review 619, and 3 exceptions are documented in IPAM ticket IPAM-2854.

- (F00984) NAT pool 10.104.166.0/28 serves outbound traffic for mailer in Aldermere, supports 54838 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00985) Subnet 10.73.12.0/24 is allocated to batch workloads in Fernhollow/dr; gateway .1, 13 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 72% at last audit.

- (F00986) Supernet 10.188.0.0/16 is delegated to Eastvale (prod) and summarised at border-3; the overlap check against Brightholm passed in review 705, and 0 exceptions are documented in IPAM ticket IPAM-2740.

- (F00987) NAT pool 10.176.110.0/28 serves outbound traffic for reports in Brightholm, supports 54942 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F00988) NAT pool 10.195.40.0/28 serves outbound traffic for catalogue in Fernhollow, supports 15218 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F00989) NAT pool 10.214.62.0/28 serves outbound traffic for ledger in Fernhollow, supports 40287 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00990) NAT pool 10.162.137.0/28 serves outbound traffic for gateway in Eastvale, supports 55288 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

## Page 111: Site allocations [addressing]

- (F00991) Supernet 10.233.0.0/16 is delegated to Brightholm (test) and summarised at border-6; the overlap check against Aldermere passed in review 809, and 1 exceptions are documented in IPAM ticket IPAM-8291.

- (F00992) NAT pool 10.40.180.0/28 serves outbound traffic for catalogue in Dunmoor, supports 24243 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F00993) NAT pool 10.214.117.0/28 serves outbound traffic for scheduler in Brightholm, supports 35733 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F00994) NAT pool 10.133.146.0/28 serves outbound traffic for mailer in Eastvale, supports 21068 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F00995) Supernet 10.253.0.0/16 is delegated to Dunmoor (mgmt) and summarised at border-2; the overlap check against Dunmoor passed in review 115, and 1 exceptions are documented in IPAM ticket IPAM-2979.

- (F00996) Supernet 10.240.48.0/20 is delegated to Cresswick (mgmt) and summarised at border-2; the overlap check against Aldermere passed in review 953, and 3 exceptions are documented in IPAM ticket IPAM-1392.

- (F00997) NAT pool 10.67.198.0/28 serves outbound traffic for reports in Brightholm, supports 23723 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F00998) NAT pool 10.150.60.0/28 serves outbound traffic for mailer in Eastvale, supports 59313 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F00999) NAT pool 10.23.37.0/28 serves outbound traffic for mailer in Eastvale, supports 29918 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

## Page 112: Management ranges [addressing]

- (F01000) NAT pool 10.244.68.0/28 serves outbound traffic for scheduler in Dunmoor, supports 47928 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F01001) Subnet 10.189.232.0/26 is allocated to bastion workloads in Brightholm/prod; gateway .1, 12 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 24% at last audit.

- (F01002) Subnet 10.24.218.0/24 is allocated to queue workloads in Cresswick/dr; gateway .1, 12 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 30% at last audit.

- (F01003) Subnet 10.142.160.0/24 is allocated to app workloads in Fernhollow/preprod; gateway .1, 13 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 48% at last audit.

- (F01004) Supernet 10.86.0.0/16 is delegated to Dunmoor (dr) and summarised at border-3; the overlap check against Eastvale passed in review 871, and 0 exceptions are documented in IPAM ticket IPAM-4795.

- (F01005) NAT pool 10.49.105.0/28 serves outbound traffic for scheduler in Cresswick, supports 2292 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F01006) NAT pool 10.3.250.0/28 serves outbound traffic for ledger in Eastvale, supports 24718 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F01007) NAT pool 10.64.232.0/28 serves outbound traffic for telemetry in Dunmoor, supports 7683 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F01008) Subnet 10.134.44.0/24 is allocated to data workloads in Dunmoor/dr; gateway .1, 10 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 40% at last audit.

## Page 113: IPv4 supernets [addressing]

- (F01009) Supernet 10.141.192.0/18 is delegated to Brightholm (mgmt) and summarised at border-6; the overlap check against Fernhollow passed in review 625, and 5 exceptions are documented in IPAM ticket IPAM-2213.

- (F01010) NAT pool 10.19.221.0/28 serves outbound traffic for catalogue in Fernhollow, supports 46709 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F01011) Subnet 10.4.125.0/26 is allocated to data workloads in Eastvale/prod; gateway .1, 20 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 45% at last audit.

- (F01012) Supernet 10.254.0.0/16 is delegated to Brightholm (dr) and summarised at border-2; the overlap check against Brightholm passed in review 750, and 0 exceptions are documented in IPAM ticket IPAM-9459.

- (F01013) NAT pool 10.1.222.0/28 serves outbound traffic for catalogue in Fernhollow, supports 32657 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F01014) Subnet 10.214.132.0/22 is allocated to bastion workloads in Fernhollow/preprod; gateway .1, 20 addresses reserved, DHCP relay to dhcp-2, growth headroom 25% and utilisation 73% at last audit.

- (F01015) NAT pool 10.153.118.0/28 serves outbound traffic for telemetry in Fernhollow, supports 44276 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F01016) NAT pool 10.182.246.0/28 serves outbound traffic for telemetry in Dunmoor, supports 6826 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F01017) Supernet 10.126.192.0/18 is delegated to Dunmoor (dr) and summarised at border-1; the overlap check against Brightholm passed in review 575, and 2 exceptions are documented in IPAM ticket IPAM-2860.

## Page 114: DHCP scopes [addressing]

- (F01018) NAT pool 10.247.250.0/28 serves outbound traffic for reports in Dunmoor, supports 45537 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F01019) Supernet 10.209.0.0/16 is delegated to Cresswick (mgmt) and summarised at border-5; the overlap check against Cresswick passed in review 367, and 5 exceptions are documented in IPAM ticket IPAM-6203.

- (F01020) Supernet 10.204.128.0/18 is delegated to Dunmoor (dr) and summarised at border-1; the overlap check against Cresswick passed in review 597, and 5 exceptions are documented in IPAM ticket IPAM-4587.

- (F01021) Supernet 10.229.192.0/18 is delegated to Fernhollow (prod) and summarised at border-2; the overlap check against Eastvale passed in review 996, and 1 exceptions are documented in IPAM ticket IPAM-9782.

- (F01022) Subnet 10.168.66.0/26 is allocated to web workloads in Fernhollow/prod; gateway .1, 2 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 57% at last audit.

- (F01023) NAT pool 10.107.185.0/28 serves outbound traffic for gateway in Aldermere, supports 10788 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F01024) NAT pool 10.82.191.0/28 serves outbound traffic for mailer in Brightholm, supports 27592 concurrent translations, timeout 60s, and is monitored with an alert at 90% port exhaustion.

- (F01025) NAT pool 10.18.10.0/28 serves outbound traffic for catalogue in Brightholm, supports 33366 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F01026) Subnet 10.12.117.0/24 is allocated to cache workloads in Brightholm/test; gateway .1, 3 addresses reserved, DHCP relay to dhcp-3, growth headroom 15% and utilisation 60% at last audit.

## Page 115: Management ranges [addressing]

- (F01027) Subnet 10.39.36.0/22 is allocated to bastion workloads in Fernhollow/test; gateway .1, 2 addresses reserved, DHCP relay to dhcp-1, growth headroom 20% and utilisation 24% at last audit.

- (F01028) NAT pool 10.99.159.0/28 serves outbound traffic for mailer in Eastvale, supports 28362 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F01029) Subnet 10.103.51.0/24 is allocated to queue workloads in Cresswick/test; gateway .1, 20 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 66% at last audit.

- (F01030) Subnet 10.142.247.0/26 is allocated to queue workloads in Brightholm/dr; gateway .1, 19 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 75% at last audit.

- (F01031) NAT pool 10.55.231.0/28 serves outbound traffic for gateway in Dunmoor, supports 38371 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F01032) Subnet 10.55.159.0/24 is allocated to batch workloads in Dunmoor/test; gateway .1, 6 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 38% at last audit.

- (F01033) Supernet 10.72.0.0/16 is delegated to Eastvale (preprod) and summarised at border-5; the overlap check against Dunmoor passed in review 635, and 5 exceptions are documented in IPAM ticket IPAM-4808.

- (F01034) Subnet 10.159.172.0/24 is allocated to data workloads in Dunmoor/test; gateway .1, 3 addresses reserved, DHCP relay to dhcp-3, growth headroom 30% and utilisation 12% at last audit.

- (F01035) Supernet 10.250.240.0/20 is delegated to Fernhollow (preprod) and summarised at border-3; the overlap check against Fernhollow passed in review 341, and 2 exceptions are documented in IPAM ticket IPAM-8559.

## Page 116: Management ranges [addressing]

- (F01036) NAT pool 10.53.217.0/28 serves outbound traffic for catalogue in Eastvale, supports 25120 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F01037) Subnet 10.101.224.0/22 is allocated to app workloads in Eastvale/prod; gateway .1, 3 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 79% at last audit.

- (F01038) Supernet 10.204.0.0/18 is delegated to Brightholm (mgmt) and summarised at border-3; the overlap check against Aldermere passed in review 545, and 2 exceptions are documented in IPAM ticket IPAM-5441.

- (F01039) NAT pool 10.190.84.0/28 serves outbound traffic for scheduler in Cresswick, supports 19518 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F01040) Subnet 10.128.241.0/26 is allocated to monitoring workloads in Eastvale/test; gateway .1, 8 addresses reserved, DHCP relay to dhcp-3, growth headroom 20% and utilisation 33% at last audit.

- (F01041) NAT pool 10.5.162.0/28 serves outbound traffic for reports in Fernhollow, supports 12245 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F01042) Subnet 10.96.102.0/26 is allocated to app workloads in Aldermere/test; gateway .1, 19 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 19% at last audit.

- (F01043) NAT pool 10.80.34.0/28 serves outbound traffic for mailer in Dunmoor, supports 42203 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F01044) Supernet 10.140.0.0/16 is delegated to Fernhollow (prod) and summarised at border-4; the overlap check against Eastvale passed in review 846, and 2 exceptions are documented in IPAM ticket IPAM-7017.

## Page 117: NAT pools [addressing]

- (F01045) Supernet 10.103.32.0/20 is delegated to Cresswick (mgmt) and summarised at border-5; the overlap check against Brightholm passed in review 205, and 5 exceptions are documented in IPAM ticket IPAM-4546.

- (F01046) Supernet 10.52.64.0/20 is delegated to Brightholm (test) and summarised at border-5; the overlap check against Eastvale passed in review 760, and 6 exceptions are documented in IPAM ticket IPAM-7274.

- (F01047) Supernet 10.141.240.0/20 is delegated to Eastvale (mgmt) and summarised at border-2; the overlap check against Brightholm passed in review 102, and 6 exceptions are documented in IPAM ticket IPAM-4798.

- (F01048) Subnet 10.73.84.0/22 is allocated to monitoring workloads in Aldermere/mgmt; gateway .1, 2 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 29% at last audit.

- (F01049) NAT pool 10.241.167.0/28 serves outbound traffic for telemetry in Dunmoor, supports 33292 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F01050) NAT pool 10.197.242.0/28 serves outbound traffic for mailer in Dunmoor, supports 20931 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F01051) NAT pool 10.109.85.0/28 serves outbound traffic for telemetry in Aldermere, supports 47118 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F01052) NAT pool 10.128.61.0/28 serves outbound traffic for reports in Dunmoor, supports 43235 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01053) Subnet 10.177.217.0/26 is allocated to cache workloads in Cresswick/dr; gateway .1, 19 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 34% at last audit.

## Page 118: IPv4 supernets [addressing]

- (F01054) Subnet 10.99.2.0/26 is allocated to queue workloads in Dunmoor/test; gateway .1, 12 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 76% at last audit.

- (F01055) Subnet 10.140.244.0/22 is allocated to bastion workloads in Eastvale/test; gateway .1, 3 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 85% at last audit.

- (F01056) Subnet 10.232.251.0/26 is allocated to data workloads in Fernhollow/dr; gateway .1, 17 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 15% at last audit.

- (F01057) NAT pool 10.90.67.0/28 serves outbound traffic for catalogue in Fernhollow, supports 27997 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F01058) Supernet 10.49.128.0/18 is delegated to Fernhollow (prod) and summarised at border-2; the overlap check against Fernhollow passed in review 728, and 5 exceptions are documented in IPAM ticket IPAM-1273.

- (F01059) Supernet 10.86.176.0/20 is delegated to Fernhollow (test) and summarised at border-5; the overlap check against Aldermere passed in review 780, and 3 exceptions are documented in IPAM ticket IPAM-7821.

- (F01060) NAT pool 10.33.98.0/28 serves outbound traffic for scheduler in Fernhollow, supports 48272 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01061) Subnet 10.101.209.0/24 is allocated to data workloads in Dunmoor/prod; gateway .1, 2 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 27% at last audit.

- (F01062) Supernet 10.44.224.0/20 is delegated to Dunmoor (mgmt) and summarised at border-1; the overlap check against Aldermere passed in review 192, and 1 exceptions are documented in IPAM ticket IPAM-2415.

## Page 119: Site allocations [addressing]

- (F01063) Supernet 10.5.0.0/16 is delegated to Eastvale (prod) and summarised at border-6; the overlap check against Cresswick passed in review 571, and 0 exceptions are documented in IPAM ticket IPAM-5042.

- (F01064) Supernet 10.67.144.0/20 is delegated to Fernhollow (preprod) and summarised at border-1; the overlap check against Dunmoor passed in review 822, and 2 exceptions are documented in IPAM ticket IPAM-3916.

- (F01065) Supernet 10.211.64.0/18 is delegated to Brightholm (mgmt) and summarised at border-2; the overlap check against Cresswick passed in review 304, and 1 exceptions are documented in IPAM ticket IPAM-5832.

- (F01066) Supernet 10.47.192.0/18 is delegated to Fernhollow (dr) and summarised at border-3; the overlap check against Eastvale passed in review 472, and 2 exceptions are documented in IPAM ticket IPAM-9569.

- (F01067) Supernet 10.197.0.0/16 is delegated to Fernhollow (preprod) and summarised at border-5; the overlap check against Eastvale passed in review 315, and 5 exceptions are documented in IPAM ticket IPAM-8108.

- (F01068) Supernet 10.175.0.0/16 is delegated to Fernhollow (test) and summarised at border-1; the overlap check against Eastvale passed in review 891, and 1 exceptions are documented in IPAM ticket IPAM-5230.

- (F01069) Subnet 10.59.92.0/22 is allocated to monitoring workloads in Dunmoor/test; gateway .1, 6 addresses reserved, DHCP relay to dhcp-4, growth headroom 25% and utilisation 59% at last audit.

- (F01070) NAT pool 10.17.165.0/28 serves outbound traffic for catalogue in Dunmoor, supports 41753 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01071) Subnet 10.172.51.0/24 is allocated to data workloads in Dunmoor/dr; gateway .1, 13 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 81% at last audit.

## Page 120: Site allocations [addressing]

- (F01072) Subnet 10.222.204.0/24 is allocated to monitoring workloads in Dunmoor/mgmt; gateway .1, 9 addresses reserved, DHCP relay to dhcp-3, growth headroom 25% and utilisation 88% at last audit.

- (F01073) Supernet 10.20.64.0/18 is delegated to Dunmoor (dr) and summarised at border-5; the overlap check against Aldermere passed in review 531, and 3 exceptions are documented in IPAM ticket IPAM-5413.

- (F01074) NAT pool 10.14.83.0/28 serves outbound traffic for scheduler in Dunmoor, supports 20198 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F01075) NAT pool 10.71.66.0/28 serves outbound traffic for mailer in Brightholm, supports 52179 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F01076) Supernet 10.202.64.0/18 is delegated to Brightholm (test) and summarised at border-4; the overlap check against Aldermere passed in review 774, and 1 exceptions are documented in IPAM ticket IPAM-4283.

- (F01077) Subnet 10.94.120.0/22 is allocated to cache workloads in Cresswick/test; gateway .1, 15 addresses reserved, DHCP relay to dhcp-1, growth headroom 20% and utilisation 31% at last audit.

- (F01078) NAT pool 10.2.244.0/28 serves outbound traffic for scheduler in Eastvale, supports 23091 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F01079) NAT pool 10.108.241.0/28 serves outbound traffic for reports in Fernhollow, supports 54983 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F01080) Subnet 10.162.68.0/22 is allocated to bastion workloads in Aldermere/dr; gateway .1, 12 addresses reserved, DHCP relay to dhcp-3, growth headroom 30% and utilisation 88% at last audit.

## Page 121: Management ranges [addressing]

- (F01081) NAT pool 10.250.13.0/28 serves outbound traffic for gateway in Aldermere, supports 58537 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F01082) Subnet 10.0.203.0/24 is allocated to app workloads in Cresswick/test; gateway .1, 9 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 17% at last audit.

- (F01083) Subnet 10.173.196.0/22 is allocated to data workloads in Cresswick/dr; gateway .1, 15 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 61% at last audit.

- (F01084) NAT pool 10.133.215.0/28 serves outbound traffic for scheduler in Dunmoor, supports 11217 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F01085) NAT pool 10.42.177.0/28 serves outbound traffic for catalogue in Aldermere, supports 43483 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01086) Subnet 10.196.232.0/26 is allocated to web workloads in Cresswick/preprod; gateway .1, 17 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 50% at last audit.

- (F01087) Supernet 10.230.176.0/20 is delegated to Cresswick (prod) and summarised at border-4; the overlap check against Fernhollow passed in review 443, and 6 exceptions are documented in IPAM ticket IPAM-9765.

- (F01088) Supernet 10.196.0.0/18 is delegated to Aldermere (preprod) and summarised at border-2; the overlap check against Aldermere passed in review 445, and 5 exceptions are documented in IPAM ticket IPAM-5224.

- (F01089) Subnet 10.232.222.0/26 is allocated to web workloads in Eastvale/mgmt; gateway .1, 16 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 74% at last audit.

## Page 122: Management ranges [addressing]

- (F01090) Supernet 10.189.128.0/20 is delegated to Aldermere (mgmt) and summarised at border-4; the overlap check against Cresswick passed in review 791, and 2 exceptions are documented in IPAM ticket IPAM-1385.

- (F01091) NAT pool 10.150.182.0/28 serves outbound traffic for reports in Cresswick, supports 1648 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F01092) Supernet 10.57.176.0/20 is delegated to Fernhollow (prod) and summarised at border-6; the overlap check against Aldermere passed in review 644, and 5 exceptions are documented in IPAM ticket IPAM-7491.

- (F01093) Subnet 10.48.64.0/26 is allocated to data workloads in Brightholm/prod; gateway .1, 17 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 70% at last audit.

- (F01094) NAT pool 10.234.20.0/28 serves outbound traffic for catalogue in Eastvale, supports 21903 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01095) Subnet 10.40.172.0/24 is allocated to queue workloads in Eastvale/prod; gateway .1, 15 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 44% at last audit.

- (F01096) NAT pool 10.221.59.0/28 serves outbound traffic for gateway in Fernhollow, supports 37914 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F01097) NAT pool 10.124.25.0/28 serves outbound traffic for mailer in Eastvale, supports 38074 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01098) Supernet 10.23.192.0/18 is delegated to Cresswick (preprod) and summarised at border-2; the overlap check against Fernhollow passed in review 391, and 2 exceptions are documented in IPAM ticket IPAM-1082.

## Page 123: Management ranges [addressing]

- (F01099) Subnet 10.66.140.0/26 is allocated to queue workloads in Aldermere/dr; gateway .1, 16 addresses reserved, DHCP disabled, growth headroom 20% and utilisation 40% at last audit.

- (F01100) Subnet 10.32.144.0/22 is allocated to monitoring workloads in Fernhollow/test; gateway .1, 20 addresses reserved, DHCP relay to dhcp-4, growth headroom 25% and utilisation 81% at last audit.

- (F01101) Supernet 10.175.0.0/16 is delegated to Dunmoor (mgmt) and summarised at border-3; the overlap check against Cresswick passed in review 942, and 3 exceptions are documented in IPAM ticket IPAM-3486.

- (F01102) Supernet 10.87.0.0/16 is delegated to Fernhollow (dr) and summarised at border-3; the overlap check against Dunmoor passed in review 133, and 5 exceptions are documented in IPAM ticket IPAM-2287.

- (F01103) NAT pool 10.176.42.0/28 serves outbound traffic for gateway in Dunmoor, supports 49521 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F01104) Supernet 10.239.0.0/18 is delegated to Cresswick (test) and summarised at border-2; the overlap check against Eastvale passed in review 698, and 1 exceptions are documented in IPAM ticket IPAM-6761.

- (F01105) NAT pool 10.11.145.0/28 serves outbound traffic for identity in Dunmoor, supports 15882 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F01106) Subnet 10.49.200.0/22 is allocated to cache workloads in Dunmoor/mgmt; gateway .1, 8 addresses reserved, DHCP relay to dhcp-1, growth headroom 25% and utilisation 34% at last audit.

- (F01107) Subnet 10.209.180.0/26 is allocated to cache workloads in Fernhollow/dr; gateway .1, 15 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 25% at last audit.

## Page 124: DHCP scopes [addressing]

- (F01108) NAT pool 10.200.115.0/28 serves outbound traffic for reports in Eastvale, supports 32929 concurrent translations, timeout 300s, and is monitored with an alert at 80% port exhaustion.

- (F01109) Supernet 10.147.0.0/18 is delegated to Brightholm (preprod) and summarised at border-5; the overlap check against Cresswick passed in review 881, and 3 exceptions are documented in IPAM ticket IPAM-3822.

- (F01110) NAT pool 10.214.214.0/28 serves outbound traffic for reports in Aldermere, supports 12878 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F01111) NAT pool 10.41.209.0/28 serves outbound traffic for ledger in Brightholm, supports 21800 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

- (F01112) Subnet 10.46.189.0/26 is allocated to web workloads in Eastvale/dr; gateway .1, 14 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 59% at last audit.

- (F01113) NAT pool 10.241.102.0/28 serves outbound traffic for mailer in Brightholm, supports 9193 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01114) Subnet 10.235.125.0/24 is allocated to monitoring workloads in Brightholm/mgmt; gateway .1, 9 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 54% at last audit.

- (F01115) Subnet 10.35.3.0/26 is allocated to web workloads in Brightholm/dr; gateway .1, 15 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 65% at last audit.

- (F01116) Supernet 10.12.0.0/16 is delegated to Fernhollow (mgmt) and summarised at border-4; the overlap check against Fernhollow passed in review 161, and 2 exceptions are documented in IPAM ticket IPAM-7527.

## Page 125: IPv4 supernets [addressing]

- (F01117) Supernet 10.225.208.0/20 is delegated to Dunmoor (mgmt) and summarised at border-1; the overlap check against Aldermere passed in review 249, and 6 exceptions are documented in IPAM ticket IPAM-5300.

- (F01118) NAT pool 10.187.211.0/28 serves outbound traffic for mailer in Aldermere, supports 9802 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F01119) Subnet 10.37.234.0/24 is allocated to monitoring workloads in Cresswick/prod; gateway .1, 9 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 68% at last audit.

- (F01120) Supernet 10.140.16.0/20 is delegated to Dunmoor (test) and summarised at border-2; the overlap check against Brightholm passed in review 634, and 2 exceptions are documented in IPAM ticket IPAM-1425.

- (F01121) Subnet 10.149.157.0/24 is allocated to data workloads in Cresswick/mgmt; gateway .1, 20 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 49% at last audit.

- (F01122) Subnet 10.149.196.0/22 is allocated to queue workloads in Fernhollow/preprod; gateway .1, 9 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 30% at last audit.

- (F01123) NAT pool 10.186.207.0/28 serves outbound traffic for identity in Aldermere, supports 41031 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F01124) NAT pool 10.160.191.0/28 serves outbound traffic for reports in Brightholm, supports 57215 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F01125) Subnet 10.247.192.0/22 is allocated to web workloads in Eastvale/dr; gateway .1, 4 addresses reserved, DHCP disabled, growth headroom 25% and utilisation 38% at last audit.

## Page 126: Site allocations [addressing]

- (F01126) Subnet 10.61.100.0/26 is allocated to batch workloads in Cresswick/mgmt; gateway .1, 17 addresses reserved, DHCP relay to dhcp-4, growth headroom 15% and utilisation 79% at last audit.

- (F01127) Subnet 10.16.204.0/24 is allocated to app workloads in Fernhollow/preprod; gateway .1, 12 addresses reserved, DHCP enabled with 8h lease, growth headroom 15% and utilisation 19% at last audit.

- (F01128) Supernet 10.125.0.0/16 is delegated to Eastvale (mgmt) and summarised at border-6; the overlap check against Brightholm passed in review 806, and 5 exceptions are documented in IPAM ticket IPAM-5015.

- (F01129) Subnet 10.20.136.0/22 is allocated to queue workloads in Fernhollow/dr; gateway .1, 4 addresses reserved, DHCP relay to dhcp-2, growth headroom 15% and utilisation 28% at last audit.

- (F01130) NAT pool 10.106.116.0/28 serves outbound traffic for gateway in Cresswick, supports 38882 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F01131) Supernet 10.163.0.0/16 is delegated to Aldermere (mgmt) and summarised at border-2; the overlap check against Dunmoor passed in review 219, and 3 exceptions are documented in IPAM ticket IPAM-2366.

- (F01132) Supernet 10.110.240.0/20 is delegated to Brightholm (prod) and summarised at border-3; the overlap check against Eastvale passed in review 109, and 4 exceptions are documented in IPAM ticket IPAM-8041.

- (F01133) Subnet 10.99.233.0/26 is allocated to web workloads in Fernhollow/dr; gateway .1, 10 addresses reserved, DHCP relay to dhcp-4, growth headroom 25% and utilisation 75% at last audit.

- (F01134) NAT pool 10.247.145.0/28 serves outbound traffic for telemetry in Brightholm, supports 17814 concurrent translations, timeout 3600s, and is monitored with an alert at 70% port exhaustion.

## Page 127: DHCP scopes [addressing]

- (F01135) Supernet 10.158.224.0/20 is delegated to Fernhollow (mgmt) and summarised at border-1; the overlap check against Brightholm passed in review 599, and 0 exceptions are documented in IPAM ticket IPAM-6229.

- (F01136) NAT pool 10.83.91.0/28 serves outbound traffic for catalogue in Dunmoor, supports 50336 concurrent translations, timeout 300s, and is monitored with an alert at 90% port exhaustion.

- (F01137) Supernet 10.93.64.0/18 is delegated to Aldermere (dr) and summarised at border-1; the overlap check against Brightholm passed in review 318, and 2 exceptions are documented in IPAM ticket IPAM-9221.

- (F01138) Supernet 10.52.128.0/18 is delegated to Cresswick (mgmt) and summarised at border-5; the overlap check against Brightholm passed in review 684, and 5 exceptions are documented in IPAM ticket IPAM-3532.

- (F01139) Supernet 10.87.64.0/18 is delegated to Brightholm (preprod) and summarised at border-5; the overlap check against Fernhollow passed in review 260, and 2 exceptions are documented in IPAM ticket IPAM-9461.

- (F01140) Supernet 10.137.64.0/18 is delegated to Fernhollow (mgmt) and summarised at border-3; the overlap check against Dunmoor passed in review 976, and 6 exceptions are documented in IPAM ticket IPAM-5974.

- (F01141) Supernet 10.181.128.0/18 is delegated to Brightholm (test) and summarised at border-4; the overlap check against Cresswick passed in review 535, and 4 exceptions are documented in IPAM ticket IPAM-7447.

- (F01142) Supernet 10.209.0.0/16 is delegated to Aldermere (dr) and summarised at border-6; the overlap check against Brightholm passed in review 567, and 6 exceptions are documented in IPAM ticket IPAM-5492.

- (F01143) Subnet 10.131.148.0/22 is allocated to batch workloads in Fernhollow/preprod; gateway .1, 2 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 53% at last audit.

## Page 128: NAT pools [addressing]

- (F01144) NAT pool 10.110.225.0/28 serves outbound traffic for telemetry in Fernhollow, supports 7501 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F01145) Subnet 10.240.23.0/26 is allocated to bastion workloads in Cresswick/dr; gateway .1, 17 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 19% at last audit.

- (F01146) Subnet 10.189.224.0/24 is allocated to queue workloads in Aldermere/test; gateway .1, 5 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 53% at last audit.

- (F01147) NAT pool 10.77.153.0/28 serves outbound traffic for gateway in Dunmoor, supports 37320 concurrent translations, timeout 60s, and is monitored with an alert at 80% port exhaustion.

- (F01148) Subnet 10.133.149.0/26 is allocated to web workloads in Cresswick/mgmt; gateway .1, 6 addresses reserved, DHCP relay to dhcp-1, growth headroom 25% and utilisation 58% at last audit.

- (F01149) Supernet 10.164.0.0/16 is delegated to Fernhollow (preprod) and summarised at border-2; the overlap check against Dunmoor passed in review 470, and 2 exceptions are documented in IPAM ticket IPAM-4260.

- (F01150) NAT pool 10.130.11.0/28 serves outbound traffic for scheduler in Fernhollow, supports 8311 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F01151) Supernet 10.30.0.0/16 is delegated to Dunmoor (dr) and summarised at border-1; the overlap check against Eastvale passed in review 547, and 0 exceptions are documented in IPAM ticket IPAM-9261.

- (F01152) Supernet 10.170.0.0/18 is delegated to Eastvale (dr) and summarised at border-6; the overlap check against Aldermere passed in review 678, and 0 exceptions are documented in IPAM ticket IPAM-2840.

## Page 129: NAT pools [addressing]

- (F01153) Subnet 10.239.97.0/26 is allocated to app workloads in Eastvale/prod; gateway .1, 15 addresses reserved, DHCP enabled with 8h lease, growth headroom 30% and utilisation 31% at last audit.

- (F01154) NAT pool 10.93.173.0/28 serves outbound traffic for identity in Cresswick, supports 35084 concurrent translations, timeout 3600s, and is monitored with an alert at 90% port exhaustion.

- (F01155) Supernet 10.150.0.0/20 is delegated to Aldermere (dr) and summarised at border-5; the overlap check against Dunmoor passed in review 119, and 0 exceptions are documented in IPAM ticket IPAM-4690.

- (F01156) Supernet 10.114.128.0/18 is delegated to Dunmoor (preprod) and summarised at border-5; the overlap check against Dunmoor passed in review 769, and 5 exceptions are documented in IPAM ticket IPAM-4282.

- (F01157) NAT pool 10.78.96.0/28 serves outbound traffic for scheduler in Cresswick, supports 14009 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01158) Subnet 10.20.65.0/26 is allocated to batch workloads in Aldermere/mgmt; gateway .1, 4 addresses reserved, DHCP enabled with 8h lease, growth headroom 20% and utilisation 38% at last audit.

- (F01159) Subnet 10.138.119.0/24 is allocated to cache workloads in Cresswick/preprod; gateway .1, 13 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 27% at last audit.

- (F01160) Supernet 10.106.192.0/20 is delegated to Aldermere (dr) and summarised at border-1; the overlap check against Dunmoor passed in review 549, and 3 exceptions are documented in IPAM ticket IPAM-4254.

- (F01161) Subnet 10.47.88.0/22 is allocated to app workloads in Dunmoor/mgmt; gateway .1, 7 addresses reserved, DHCP disabled, growth headroom 30% and utilisation 57% at last audit.

## Page 130: DHCP scopes [addressing]

- (F01162) Supernet 10.184.0.0/16 is delegated to Brightholm (preprod) and summarised at border-3; the overlap check against Eastvale passed in review 214, and 3 exceptions are documented in IPAM ticket IPAM-1264.

- (F01163) Subnet 10.51.181.0/24 is allocated to batch workloads in Dunmoor/dr; gateway .1, 11 addresses reserved, DHCP enabled with 8h lease, growth headroom 25% and utilisation 41% at last audit.

- (F01164) NAT pool 10.241.8.0/28 serves outbound traffic for telemetry in Aldermere, supports 48316 concurrent translations, timeout 3600s, and is monitored with an alert at 80% port exhaustion.

- (F01165) Subnet 10.4.64.0/22 is allocated to data workloads in Brightholm/preprod; gateway .1, 6 addresses reserved, DHCP disabled, growth headroom 15% and utilisation 88% at last audit.

- (F01166) Subnet 10.212.80.0/24 is allocated to bastion workloads in Fernhollow/test; gateway .1, 7 addresses reserved, DHCP relay to dhcp-2, growth headroom 20% and utilisation 35% at last audit.

- (F01167) Supernet 10.254.0.0/16 is delegated to Aldermere (preprod) and summarised at border-3; the overlap check against Dunmoor passed in review 740, and 2 exceptions are documented in IPAM ticket IPAM-5344.

- (F01168) NAT pool 10.13.169.0/28 serves outbound traffic for ledger in Cresswick, supports 58749 concurrent translations, timeout 300s, and is monitored with an alert at 70% port exhaustion.

- (F01169) NAT pool 10.23.193.0/28 serves outbound traffic for scheduler in Brightholm, supports 10865 concurrent translations, timeout 60s, and is monitored with an alert at 70% port exhaustion.

- (F01170) Supernet 10.33.0.0/18 is delegated to Brightholm (prod) and summarised at border-4; the overlap check against Dunmoor passed in review 525, and 6 exceptions are documented in IPAM ticket IPAM-9793.

## Page 131: Backup tiers [compute]

- (F01171) Cluster EAS-PROD-5 has 19 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01172) Datastore cre-ds40 provides 362 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01173) Datastore eas-ds13 provides 84 TB usable on NVMe with mirror; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01174) Cluster FER-PROD-2 has 26 hosts of model DL380g11 with 96 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01175) Cluster CRE-PREPROD-5 has 14 hosts of model SR650v3 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01176) Datastore eas-ds57 provides 156 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01177) Datastore bri-ds38 provides 397 TB usable on NVMe with mirror; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01178) Cluster BRI-PREPROD-1 has 8 hosts of model SR650v3 with 64 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01179) Workload ledger-monitoring runs 32 VMs of size 8vCPU/32GB in anti-affinity group AG-13, storage policy bronze and backup tier T3-weekly with RPO 4h.

## Page 132: Backup tiers [compute]

- (F01180) Cluster DUN-MGMT-5 has 21 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01181) Datastore cre-ds22 provides 115 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01182) Workload catalogue-batch runs 35 VMs of size 8vCPU/32GB in anti-affinity group AG-5, storage policy silver and backup tier T2-daily with RPO 24h.

- (F01183) Cluster EAS-PREPROD-2 has 11 hosts of model DL380g11 with 64 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01184) Workload scheduler-batch runs 21 VMs of size 8vCPU/32GB in anti-affinity group AG-28, storage policy bronze and backup tier T1-hourly with RPO 24h.

- (F01185) Cluster DUN-MGMT-4 has 8 hosts of model SR650v3 with 64 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01186) Datastore cre-ds34 provides 327 TB usable on NVMe with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01187) Cluster EAS-TEST-9 has 11 hosts of model SR650v3 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01188) Cluster FER-PREPROD-4 has 30 hosts of model SR650v3 with 64 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

## Page 133: Workload placement [compute]

- (F01189) Workload ledger-bastion runs 20 VMs of size 8vCPU/32GB in anti-affinity group AG-58, storage policy bronze and backup tier T2-daily with RPO 4h.

- (F01190) Workload mailer-data runs 21 VMs of size 4vCPU/16GB in anti-affinity group AG-5, storage policy silver and backup tier T3-weekly with RPO 24h.

- (F01191) Datastore cre-ds14 provides 395 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01192) Workload scheduler-data runs 32 VMs of size 4vCPU/16GB in anti-affinity group AG-49, storage policy gold and backup tier T2-daily with RPO 1h.

- (F01193) Datastore dun-ds26 provides 322 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01194) Cluster CRE-PREPROD-7 has 7 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01195) Cluster DUN-PREPROD-5 has 28 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01196) Workload catalogue-monitoring runs 16 VMs of size 16vCPU/64GB in anti-affinity group AG-29, storage policy silver and backup tier T1-hourly with RPO 24h.

- (F01197) Datastore eas-ds30 provides 98 TB usable on NVMe with mirror; thin-provisioning ratio 1.5:1 and an alert at 80% used.

## Page 134: Hypervisor clusters [compute]

- (F01198) Workload telemetry-app runs 31 VMs of size 8vCPU/32GB in anti-affinity group AG-38, storage policy gold and backup tier T3-weekly with RPO 24h.

- (F01199) Workload telemetry-cache runs 35 VMs of size 4vCPU/16GB in anti-affinity group AG-6, storage policy bronze and backup tier T3-weekly with RPO 24h.

- (F01200) Workload gateway-monitoring runs 29 VMs of size 8vCPU/32GB in anti-affinity group AG-4, storage policy bronze and backup tier T1-hourly with RPO 4h.

- (F01201) Datastore fer-ds18 provides 148 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01202) Datastore cre-ds23 provides 62 TB usable on NVMe with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01203) Cluster EAS-DR-4 has 22 hosts of model DL380g11 with 128 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01204) Workload reports-bastion runs 4 VMs of size 16vCPU/64GB in anti-affinity group AG-7, storage policy bronze and backup tier T3-weekly with RPO 1h.

- (F01205) Datastore ald-ds08 provides 142 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01206) Datastore dun-ds53 provides 221 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 80% used.

## Page 135: Backup tiers [compute]

- (F01207) Workload ledger-bastion runs 29 VMs of size 16vCPU/64GB in anti-affinity group AG-59, storage policy gold and backup tier T1-hourly with RPO 24h.

- (F01208) Cluster ALD-TEST-2 has 13 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01209) Workload mailer-batch runs 17 VMs of size 8vCPU/32GB in anti-affinity group AG-29, storage policy gold and backup tier T2-daily with RPO 4h.

- (F01210) Datastore fer-ds17 provides 102 TB usable on NVMe with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01211) Workload reports-batch runs 13 VMs of size 8vCPU/32GB in anti-affinity group AG-55, storage policy gold and backup tier T2-daily with RPO 4h.

- (F01212) Datastore eas-ds48 provides 136 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01213) Cluster FER-DR-6 has 23 hosts of model DL380g11 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01214) Workload identity-batch runs 23 VMs of size 8vCPU/32GB in anti-affinity group AG-58, storage policy silver and backup tier T1-hourly with RPO 1h.

- (F01215) Workload ledger-app runs 14 VMs of size 16vCPU/64GB in anti-affinity group AG-20, storage policy bronze and backup tier T3-weekly with RPO 24h.

## Page 136: Capacity [compute]

- (F01216) Workload scheduler-bastion runs 6 VMs of size 4vCPU/16GB in anti-affinity group AG-6, storage policy gold and backup tier T3-weekly with RPO 24h.

- (F01217) Datastore dun-ds55 provides 154 TB usable on NVMe with mirror; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01218) Workload reports-data runs 26 VMs of size 4vCPU/16GB in anti-affinity group AG-55, storage policy bronze and backup tier T2-daily with RPO 24h.

- (F01219) Datastore ald-ds21 provides 135 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01220) Cluster FER-TEST-1 has 19 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01221) Workload gateway-data runs 2 VMs of size 8vCPU/32GB in anti-affinity group AG-16, storage policy gold and backup tier T3-weekly with RPO 4h.

- (F01222) Workload reports-cache runs 28 VMs of size 4vCPU/16GB in anti-affinity group AG-55, storage policy bronze and backup tier T3-weekly with RPO 4h.

- (F01223) Datastore eas-ds57 provides 218 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01224) Workload reports-batch runs 25 VMs of size 4vCPU/16GB in anti-affinity group AG-21, storage policy bronze and backup tier T2-daily with RPO 1h.

## Page 137: Workload placement [compute]

- (F01225) Workload gateway-data runs 8 VMs of size 16vCPU/64GB in anti-affinity group AG-46, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01226) Cluster EAS-PREPROD-6 has 26 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01227) Workload ledger-monitoring runs 30 VMs of size 8vCPU/32GB in anti-affinity group AG-38, storage policy silver and backup tier T1-hourly with RPO 1h.

- (F01228) Cluster EAS-DR-9 has 24 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01229) Cluster FER-TEST-2 has 27 hosts of model DL380g11 with 128 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01230) Datastore eas-ds32 provides 240 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01231) Datastore dun-ds20 provides 295 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01232) Cluster EAS-MGMT-7 has 8 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01233) Datastore ald-ds46 provides 203 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 85% used.

## Page 138: Hypervisor clusters [compute]

- (F01234) Datastore dun-ds47 provides 102 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01235) Cluster BRI-PROD-8 has 27 hosts of model R760 with 96 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01236) Datastore fer-ds44 provides 218 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01237) Cluster CRE-PREPROD-2 has 13 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01238) Workload catalogue-data runs 18 VMs of size 8vCPU/32GB in anti-affinity group AG-13, storage policy gold and backup tier T2-daily with RPO 24h.

- (F01239) Datastore ald-ds22 provides 251 TB usable on NVMe with mirror; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01240) Datastore ald-ds36 provides 50 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01241) Cluster EAS-PROD-1 has 14 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01242) Workload catalogue-data runs 14 VMs of size 16vCPU/64GB in anti-affinity group AG-40, storage policy silver and backup tier T1-hourly with RPO 24h.

## Page 139: Workload placement [compute]

- (F01243) Workload catalogue-data runs 40 VMs of size 8vCPU/32GB in anti-affinity group AG-37, storage policy gold and backup tier T2-daily with RPO 24h.

- (F01244) Cluster EAS-PREPROD-8 has 4 hosts of model SR650v3 with 64 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01245) Workload catalogue-batch runs 13 VMs of size 16vCPU/64GB in anti-affinity group AG-34, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01246) Cluster EAS-PREPROD-6 has 18 hosts of model SR650v3 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01247) Datastore eas-ds05 provides 193 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01248) Workload gateway-bastion runs 4 VMs of size 8vCPU/32GB in anti-affinity group AG-4, storage policy silver and backup tier T3-weekly with RPO 24h.

- (F01249) Datastore ald-ds55 provides 286 TB usable on NVMe with mirror; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01250) Datastore eas-ds37 provides 379 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01251) Datastore bri-ds19 provides 184 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 80% used.

## Page 140: Backup tiers [compute]

- (F01252) Workload reports-bastion runs 7 VMs of size 8vCPU/32GB in anti-affinity group AG-2, storage policy silver and backup tier T1-hourly with RPO 4h.

- (F01253) Datastore dun-ds40 provides 219 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01254) Datastore ald-ds34 provides 41 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01255) Datastore eas-ds35 provides 108 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01256) Datastore ald-ds04 provides 175 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01257) Cluster FER-DR-9 has 20 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01258) Cluster BRI-PROD-8 has 9 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01259) Cluster DUN-PREPROD-1 has 5 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01260) Cluster BRI-TEST-3 has 16 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

## Page 141: Workload placement [compute]

- (F01261) Datastore bri-ds40 provides 362 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01262) Datastore fer-ds20 provides 124 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01263) Datastore ald-ds27 provides 231 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01264) Workload ledger-bastion runs 4 VMs of size 16vCPU/64GB in anti-affinity group AG-50, storage policy silver and backup tier T1-hourly with RPO 24h.

- (F01265) Datastore bri-ds05 provides 346 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01266) Cluster BRI-MGMT-6 has 9 hosts of model SR650v3 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01267) Workload telemetry-queue runs 20 VMs of size 16vCPU/64GB in anti-affinity group AG-17, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01268) Cluster ALD-MGMT-8 has 10 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01269) Cluster ALD-PREPROD-1 has 30 hosts of model DL380g11 with 64 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

## Page 142: Workload placement [compute]

- (F01270) Workload mailer-monitoring runs 11 VMs of size 8vCPU/32GB in anti-affinity group AG-39, storage policy gold and backup tier T3-weekly with RPO 24h.

- (F01271) Cluster BRI-TEST-1 has 22 hosts of model R760 with 64 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01272) Workload identity-cache runs 5 VMs of size 8vCPU/32GB in anti-affinity group AG-25, storage policy gold and backup tier T2-daily with RPO 24h.

- (F01273) Cluster BRI-PREPROD-4 has 14 hosts of model SR650v3 with 128 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01274) Cluster BRI-MGMT-9 has 13 hosts of model SR650v3 with 64 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01275) Cluster ALD-PROD-7 has 20 hosts of model SR650v3 with 64 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01276) Datastore cre-ds24 provides 39 TB usable on NVMe with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01277) Cluster DUN-PROD-1 has 30 hosts of model DL380g11 with 128 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01278) Cluster EAS-MGMT-2 has 4 hosts of model SR650v3 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

## Page 143: Storage policies [compute]

- (F01279) Datastore eas-ds25 provides 250 TB usable on hybrid with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01280) Datastore cre-ds23 provides 345 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01281) Datastore cre-ds15 provides 93 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01282) Workload telemetry-data runs 25 VMs of size 16vCPU/64GB in anti-affinity group AG-2, storage policy silver and backup tier T2-daily with RPO 1h.

- (F01283) Cluster DUN-DR-9 has 31 hosts of model R760 with 96 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01284) Cluster DUN-DR-7 has 18 hosts of model SR650v3 with 96 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01285) Workload mailer-batch runs 27 VMs of size 4vCPU/16GB in anti-affinity group AG-47, storage policy bronze and backup tier T1-hourly with RPO 1h.

- (F01286) Cluster FER-PREPROD-4 has 31 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01287) Datastore dun-ds24 provides 349 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

## Page 144: Backup tiers [compute]

- (F01288) Cluster EAS-DR-5 has 32 hosts of model SR650v3 with 96 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01289) Workload scheduler-bastion runs 35 VMs of size 8vCPU/32GB in anti-affinity group AG-12, storage policy silver and backup tier T1-hourly with RPO 24h.

- (F01290) Cluster DUN-MGMT-3 has 12 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01291) Workload gateway-data runs 28 VMs of size 8vCPU/32GB in anti-affinity group AG-30, storage policy gold and backup tier T3-weekly with RPO 1h.

- (F01292) Workload mailer-web runs 8 VMs of size 4vCPU/16GB in anti-affinity group AG-6, storage policy gold and backup tier T1-hourly with RPO 1h.

- (F01293) Workload catalogue-batch runs 24 VMs of size 4vCPU/16GB in anti-affinity group AG-48, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01294) Cluster CRE-MGMT-6 has 22 hosts of model DL380g11 with 96 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01295) Workload telemetry-app runs 37 VMs of size 4vCPU/16GB in anti-affinity group AG-58, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01296) Cluster EAS-MGMT-7 has 9 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

## Page 145: Storage policies [compute]

- (F01297) Datastore bri-ds08 provides 359 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01298) Cluster DUN-DR-7 has 19 hosts of model R760 with 64 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01299) Workload scheduler-monitoring runs 3 VMs of size 8vCPU/32GB in anti-affinity group AG-43, storage policy bronze and backup tier T2-daily with RPO 4h.

- (F01300) Cluster CRE-PROD-3 has 8 hosts of model SR650v3 with 96 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01301) Cluster FER-PREPROD-6 has 13 hosts of model SR650v3 with 64 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01302) Cluster EAS-MGMT-7 has 9 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01303) Datastore ald-ds32 provides 183 TB usable on NVMe with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01304) Datastore cre-ds17 provides 249 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01305) Datastore fer-ds30 provides 357 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 75% used.

## Page 146: Workload placement [compute]

- (F01306) Datastore ald-ds48 provides 313 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01307) Workload reports-bastion runs 4 VMs of size 16vCPU/64GB in anti-affinity group AG-44, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01308) Workload mailer-bastion runs 28 VMs of size 16vCPU/64GB in anti-affinity group AG-22, storage policy gold and backup tier T2-daily with RPO 24h.

- (F01309) Workload gateway-monitoring runs 20 VMs of size 8vCPU/32GB in anti-affinity group AG-6, storage policy silver and backup tier T3-weekly with RPO 1h.

- (F01310) Datastore cre-ds56 provides 280 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01311) Cluster ALD-PREPROD-6 has 6 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01312) Cluster FER-PROD-6 has 31 hosts of model SR650v3 with 64 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01313) Workload mailer-app runs 9 VMs of size 4vCPU/16GB in anti-affinity group AG-46, storage policy gold and backup tier T1-hourly with RPO 24h.

- (F01314) Cluster BRI-PROD-2 has 4 hosts of model DL380g11 with 128 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

## Page 147: Hypervisor clusters [compute]

- (F01315) Workload mailer-cache runs 32 VMs of size 4vCPU/16GB in anti-affinity group AG-46, storage policy silver and backup tier T3-weekly with RPO 24h.

- (F01316) Cluster DUN-TEST-1 has 18 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01317) Cluster CRE-PREPROD-9 has 22 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01318) Cluster BRI-TEST-4 has 9 hosts of model DL380g11 with 128 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01319) Workload telemetry-cache runs 29 VMs of size 8vCPU/32GB in anti-affinity group AG-53, storage policy silver and backup tier T3-weekly with RPO 1h.

- (F01320) Datastore ald-ds42 provides 369 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01321) Cluster ALD-DR-6 has 32 hosts of model SR650v3 with 64 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01322) Datastore fer-ds29 provides 26 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01323) Datastore cre-ds45 provides 368 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 85% used.

## Page 148: Storage policies [compute]

- (F01324) Datastore cre-ds29 provides 203 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01325) Workload identity-batch runs 36 VMs of size 16vCPU/64GB in anti-affinity group AG-13, storage policy gold and backup tier T3-weekly with RPO 1h.

- (F01326) Cluster FER-TEST-7 has 18 hosts of model DL380g11 with 96 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01327) Workload scheduler-data runs 26 VMs of size 8vCPU/32GB in anti-affinity group AG-2, storage policy gold and backup tier T2-daily with RPO 4h.

- (F01328) Datastore bri-ds26 provides 207 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01329) Cluster EAS-PREPROD-4 has 7 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01330) Workload gateway-web runs 33 VMs of size 8vCPU/32GB in anti-affinity group AG-11, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01331) Cluster BRI-DR-8 has 17 hosts of model DL380g11 with 64 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01332) Workload catalogue-app runs 22 VMs of size 16vCPU/64GB in anti-affinity group AG-31, storage policy bronze and backup tier T2-daily with RPO 1h.

## Page 149: Workload placement [compute]

- (F01333) Datastore dun-ds52 provides 130 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01334) Datastore bri-ds22 provides 342 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01335) Datastore ald-ds39 provides 86 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01336) Workload scheduler-batch runs 38 VMs of size 8vCPU/32GB in anti-affinity group AG-5, storage policy gold and backup tier T2-daily with RPO 4h.

- (F01337) Workload gateway-cache runs 22 VMs of size 16vCPU/64GB in anti-affinity group AG-15, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01338) Workload mailer-batch runs 14 VMs of size 4vCPU/16GB in anti-affinity group AG-21, storage policy bronze and backup tier T3-weekly with RPO 1h.

- (F01339) Datastore eas-ds40 provides 141 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01340) Cluster CRE-MGMT-2 has 16 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01341) Workload identity-queue runs 6 VMs of size 8vCPU/32GB in anti-affinity group AG-25, storage policy gold and backup tier T2-daily with RPO 24h.

## Page 150: Workload placement [compute]

- (F01342) Workload ledger-monitoring runs 17 VMs of size 4vCPU/16GB in anti-affinity group AG-41, storage policy gold and backup tier T2-daily with RPO 4h.

- (F01343) Datastore dun-ds36 provides 94 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01344) Datastore eas-ds13 provides 350 TB usable on NVMe with mirror; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01345) Workload ledger-cache runs 35 VMs of size 16vCPU/64GB in anti-affinity group AG-19, storage policy gold and backup tier T2-daily with RPO 4h.

- (F01346) Datastore ald-ds20 provides 153 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01347) Cluster FER-DR-2 has 15 hosts of model DL380g11 with 64 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01348) Datastore bri-ds39 provides 247 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01349) Workload gateway-monitoring runs 20 VMs of size 4vCPU/16GB in anti-affinity group AG-38, storage policy gold and backup tier T2-daily with RPO 1h.

- (F01350) Cluster ALD-TEST-9 has 19 hosts of model DL380g11 with 64 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

## Page 151: Capacity [compute]

- (F01351) Cluster FER-DR-6 has 16 hosts of model R760 with 96 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01352) Workload mailer-web runs 34 VMs of size 4vCPU/16GB in anti-affinity group AG-47, storage policy bronze and backup tier T3-weekly with RPO 1h.

- (F01353) Workload catalogue-app runs 10 VMs of size 4vCPU/16GB in anti-affinity group AG-7, storage policy bronze and backup tier T1-hourly with RPO 24h.

- (F01354) Cluster ALD-TEST-6 has 14 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01355) Workload ledger-bastion runs 27 VMs of size 16vCPU/64GB in anti-affinity group AG-10, storage policy bronze and backup tier T1-hourly with RPO 1h.

- (F01356) Workload scheduler-app runs 18 VMs of size 4vCPU/16GB in anti-affinity group AG-16, storage policy gold and backup tier T3-weekly with RPO 24h.

- (F01357) Datastore ald-ds04 provides 349 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01358) Cluster BRI-PREPROD-3 has 31 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01359) Datastore fer-ds26 provides 29 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 75% used.

## Page 152: Backup tiers [compute]

- (F01360) Datastore ald-ds03 provides 122 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01361) Datastore dun-ds01 provides 198 TB usable on hybrid with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01362) Datastore bri-ds26 provides 128 TB usable on NVMe with mirror; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01363) Datastore eas-ds19 provides 156 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01364) Cluster BRI-MGMT-5 has 14 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01365) Datastore cre-ds29 provides 34 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01366) Datastore dun-ds14 provides 114 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01367) Datastore bri-ds13 provides 311 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01368) Datastore bri-ds57 provides 323 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 75% used.

## Page 153: Workload placement [compute]

- (F01369) Datastore cre-ds14 provides 281 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01370) Cluster CRE-PREPROD-8 has 27 hosts of model DL380g11 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01371) Datastore bri-ds59 provides 271 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01372) Datastore bri-ds05 provides 335 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01373) Cluster ALD-TEST-1 has 13 hosts of model DL380g11 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01374) Cluster ALD-TEST-4 has 24 hosts of model R760 with 96 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01375) Workload reports-web runs 21 VMs of size 4vCPU/16GB in anti-affinity group AG-58, storage policy gold and backup tier T2-daily with RPO 1h.

- (F01376) Workload identity-cache runs 9 VMs of size 16vCPU/64GB in anti-affinity group AG-48, storage policy bronze and backup tier T1-hourly with RPO 4h.

- (F01377) Cluster ALD-PROD-2 has 27 hosts of model R760 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

## Page 154: Storage policies [compute]

- (F01378) Workload ledger-monitoring runs 6 VMs of size 16vCPU/64GB in anti-affinity group AG-45, storage policy gold and backup tier T1-hourly with RPO 1h.

- (F01379) Workload reports-web runs 4 VMs of size 8vCPU/32GB in anti-affinity group AG-28, storage policy silver and backup tier T2-daily with RPO 1h.

- (F01380) Cluster EAS-PROD-2 has 28 hosts of model DL380g11 with 128 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01381) Cluster CRE-PROD-5 has 31 hosts of model R760 with 64 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01382) Datastore ald-ds56 provides 308 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01383) Cluster FER-PROD-5 has 15 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01384) Datastore bri-ds24 provides 357 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01385) Cluster CRE-TEST-7 has 9 hosts of model SR650v3 with 96 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01386) Workload scheduler-monitoring runs 36 VMs of size 8vCPU/32GB in anti-affinity group AG-24, storage policy silver and backup tier T1-hourly with RPO 24h.

## Page 155: Storage policies [compute]

- (F01387) Cluster CRE-TEST-8 has 18 hosts of model SR650v3 with 128 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01388) Datastore fer-ds10 provides 326 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01389) Cluster EAS-PREPROD-4 has 30 hosts of model SR650v3 with 96 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01390) Datastore eas-ds03 provides 286 TB usable on NVMe with mirror; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01391) Datastore fer-ds11 provides 398 TB usable on NVMe with mirror; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01392) Workload catalogue-batch runs 25 VMs of size 16vCPU/64GB in anti-affinity group AG-60, storage policy silver and backup tier T3-weekly with RPO 24h.

- (F01393) Workload gateway-batch runs 28 VMs of size 16vCPU/64GB in anti-affinity group AG-49, storage policy gold and backup tier T1-hourly with RPO 24h.

- (F01394) Datastore dun-ds10 provides 375 TB usable on NVMe with mirror; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01395) Cluster DUN-PREPROD-2 has 26 hosts of model DL380g11 with 64 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

## Page 156: Capacity [compute]

- (F01396) Datastore ald-ds53 provides 117 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01397) Cluster BRI-PREPROD-2 has 6 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01398) Datastore dun-ds01 provides 377 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01399) Workload gateway-queue runs 29 VMs of size 16vCPU/64GB in anti-affinity group AG-38, storage policy silver and backup tier T3-weekly with RPO 24h.

- (F01400) Datastore ald-ds44 provides 271 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01401) Cluster CRE-DR-7 has 28 hosts of model SR650v3 with 64 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01402) Datastore cre-ds44 provides 271 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01403) Cluster DUN-TEST-9 has 6 hosts of model R760 with 64 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01404) Cluster DUN-DR-6 has 11 hosts of model SR650v3 with 96 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

## Page 157: Capacity [compute]

- (F01405) Datastore dun-ds14 provides 334 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01406) Cluster EAS-PROD-9 has 18 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01407) Datastore eas-ds25 provides 294 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01408) Datastore ald-ds45 provides 284 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01409) Cluster ALD-TEST-6 has 17 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01410) Workload identity-cache runs 2 VMs of size 8vCPU/32GB in anti-affinity group AG-50, storage policy bronze and backup tier T3-weekly with RPO 1h.

- (F01411) Workload ledger-queue runs 13 VMs of size 4vCPU/16GB in anti-affinity group AG-22, storage policy bronze and backup tier T3-weekly with RPO 4h.

- (F01412) Cluster FER-DR-2 has 7 hosts of model R760 with 64 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01413) Datastore ald-ds29 provides 274 TB usable on SAS SSD with mirror; thin-provisioning ratio 1.5:1 and an alert at 75% used.

## Page 158: Capacity [compute]

- (F01414) Datastore cre-ds41 provides 298 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01415) Workload reports-bastion runs 6 VMs of size 4vCPU/16GB in anti-affinity group AG-6, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01416) Workload reports-cache runs 10 VMs of size 4vCPU/16GB in anti-affinity group AG-2, storage policy gold and backup tier T1-hourly with RPO 24h.

- (F01417) Cluster FER-PREPROD-8 has 25 hosts of model SR650v3 with 96 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01418) Cluster FER-PREPROD-7 has 7 hosts of model SR650v3 with 64 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01419) Workload scheduler-bastion runs 2 VMs of size 8vCPU/32GB in anti-affinity group AG-4, storage policy bronze and backup tier T1-hourly with RPO 1h.

- (F01420) Datastore fer-ds18 provides 319 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01421) Workload gateway-monitoring runs 15 VMs of size 4vCPU/16GB in anti-affinity group AG-43, storage policy silver and backup tier T2-daily with RPO 4h.

- (F01422) Cluster ALD-PREPROD-7 has 21 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

## Page 159: Workload placement [compute]

- (F01423) Datastore bri-ds56 provides 54 TB usable on SAS SSD with mirror; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01424) Cluster BRI-DR-6 has 11 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01425) Workload reports-web runs 14 VMs of size 16vCPU/64GB in anti-affinity group AG-47, storage policy silver and backup tier T2-daily with RPO 4h.

- (F01426) Datastore bri-ds48 provides 85 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01427) Datastore fer-ds11 provides 143 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01428) Cluster DUN-MGMT-1 has 17 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01429) Datastore ald-ds24 provides 162 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01430) Workload telemetry-batch runs 21 VMs of size 8vCPU/32GB in anti-affinity group AG-33, storage policy silver and backup tier T2-daily with RPO 24h.

- (F01431) Datastore fer-ds36 provides 369 TB usable on hybrid with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

## Page 160: Workload placement [compute]

- (F01432) Workload mailer-app runs 33 VMs of size 8vCPU/32GB in anti-affinity group AG-35, storage policy bronze and backup tier T3-weekly with RPO 24h.

- (F01433) Cluster CRE-TEST-5 has 31 hosts of model DL380g11 with 128 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01434) Workload gateway-cache runs 24 VMs of size 8vCPU/32GB in anti-affinity group AG-13, storage policy silver and backup tier T3-weekly with RPO 24h.

- (F01435) Workload telemetry-queue runs 40 VMs of size 8vCPU/32GB in anti-affinity group AG-43, storage policy bronze and backup tier T1-hourly with RPO 24h.

- (F01436) Cluster FER-TEST-4 has 25 hosts of model SR650v3 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01437) Workload gateway-monitoring runs 39 VMs of size 16vCPU/64GB in anti-affinity group AG-12, storage policy gold and backup tier T3-weekly with RPO 24h.

- (F01438) Workload gateway-cache runs 40 VMs of size 16vCPU/64GB in anti-affinity group AG-54, storage policy silver and backup tier T1-hourly with RPO 24h.

- (F01439) Workload mailer-cache runs 27 VMs of size 8vCPU/32GB in anti-affinity group AG-46, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01440) Datastore cre-ds10 provides 150 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

## Page 161: Backup tiers [compute]

- (F01441) Datastore dun-ds01 provides 54 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01442) Datastore eas-ds53 provides 161 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01443) Workload ledger-bastion runs 33 VMs of size 16vCPU/64GB in anti-affinity group AG-7, storage policy silver and backup tier T2-daily with RPO 4h.

- (F01444) Workload catalogue-data runs 13 VMs of size 4vCPU/16GB in anti-affinity group AG-24, storage policy gold and backup tier T1-hourly with RPO 1h.

- (F01445) Workload catalogue-queue runs 10 VMs of size 4vCPU/16GB in anti-affinity group AG-60, storage policy bronze and backup tier T3-weekly with RPO 4h.

- (F01446) Cluster ALD-MGMT-1 has 4 hosts of model R760 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01447) Workload reports-cache runs 16 VMs of size 4vCPU/16GB in anti-affinity group AG-40, storage policy bronze and backup tier T3-weekly with RPO 4h.

- (F01448) Datastore cre-ds54 provides 141 TB usable on NVMe with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01449) Workload gateway-data runs 26 VMs of size 4vCPU/16GB in anti-affinity group AG-35, storage policy bronze and backup tier T1-hourly with RPO 1h.

## Page 162: Hypervisor clusters [compute]

- (F01450) Datastore fer-ds40 provides 158 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01451) Workload gateway-cache runs 31 VMs of size 16vCPU/64GB in anti-affinity group AG-11, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01452) Cluster ALD-PREPROD-5 has 17 hosts of model SR650v3 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01453) Cluster ALD-PROD-7 has 26 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01454) Datastore dun-ds02 provides 297 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01455) Workload mailer-batch runs 3 VMs of size 8vCPU/32GB in anti-affinity group AG-33, storage policy bronze and backup tier T2-daily with RPO 4h.

- (F01456) Datastore bri-ds24 provides 93 TB usable on hybrid with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01457) Datastore dun-ds11 provides 226 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01458) Workload telemetry-cache runs 20 VMs of size 4vCPU/16GB in anti-affinity group AG-25, storage policy bronze and backup tier T2-daily with RPO 1h.

## Page 163: Capacity [compute]

- (F01459) Cluster FER-PROD-8 has 26 hosts of model R760 with 96 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01460) Workload ledger-monitoring runs 29 VMs of size 16vCPU/64GB in anti-affinity group AG-29, storage policy silver and backup tier T1-hourly with RPO 4h.

- (F01461) Workload mailer-cache runs 19 VMs of size 8vCPU/32GB in anti-affinity group AG-59, storage policy silver and backup tier T2-daily with RPO 1h.

- (F01462) Cluster BRI-MGMT-9 has 23 hosts of model SR650v3 with 64 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01463) Cluster BRI-PROD-3 has 6 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01464) Cluster EAS-TEST-8 has 8 hosts of model DL380g11 with 64 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01465) Cluster DUN-TEST-3 has 20 hosts of model R760 with 64 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01466) Datastore fer-ds51 provides 399 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01467) Workload scheduler-cache runs 3 VMs of size 4vCPU/16GB in anti-affinity group AG-39, storage policy bronze and backup tier T1-hourly with RPO 1h.

## Page 164: Hypervisor clusters [compute]

- (F01468) Workload scheduler-app runs 31 VMs of size 16vCPU/64GB in anti-affinity group AG-49, storage policy silver and backup tier T3-weekly with RPO 1h.

- (F01469) Cluster EAS-PREPROD-4 has 29 hosts of model R760 with 96 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01470) Cluster EAS-MGMT-1 has 16 hosts of model R760 with 64 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01471) Cluster BRI-MGMT-6 has 22 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01472) Datastore ald-ds46 provides 147 TB usable on NVMe with mirror; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01473) Cluster DUN-PREPROD-1 has 13 hosts of model DL380g11 with 128 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01474) Datastore eas-ds47 provides 226 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01475) Workload reports-queue runs 35 VMs of size 8vCPU/32GB in anti-affinity group AG-11, storage policy bronze and backup tier T2-daily with RPO 1h.

- (F01476) Cluster BRI-PROD-6 has 30 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

## Page 165: Backup tiers [compute]

- (F01477) Workload mailer-web runs 22 VMs of size 8vCPU/32GB in anti-affinity group AG-13, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01478) Datastore bri-ds29 provides 322 TB usable on hybrid with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01479) Workload gateway-data runs 3 VMs of size 4vCPU/16GB in anti-affinity group AG-58, storage policy silver and backup tier T2-daily with RPO 4h.

- (F01480) Workload identity-monitoring runs 25 VMs of size 4vCPU/16GB in anti-affinity group AG-30, storage policy gold and backup tier T2-daily with RPO 1h.

- (F01481) Cluster BRI-PROD-5 has 15 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01482) Workload catalogue-queue runs 24 VMs of size 16vCPU/64GB in anti-affinity group AG-36, storage policy silver and backup tier T1-hourly with RPO 4h.

- (F01483) Cluster CRE-TEST-4 has 13 hosts of model SR650v3 with 64 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01484) Datastore fer-ds36 provides 158 TB usable on NVMe with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01485) Datastore eas-ds24 provides 32 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 85% used.

## Page 166: Backup tiers [compute]

- (F01486) Workload mailer-queue runs 25 VMs of size 4vCPU/16GB in anti-affinity group AG-52, storage policy bronze and backup tier T3-weekly with RPO 1h.

- (F01487) Workload identity-bastion runs 34 VMs of size 4vCPU/16GB in anti-affinity group AG-43, storage policy bronze and backup tier T3-weekly with RPO 24h.

- (F01488) Datastore eas-ds05 provides 98 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01489) Workload telemetry-data runs 11 VMs of size 4vCPU/16GB in anti-affinity group AG-6, storage policy bronze and backup tier T2-daily with RPO 4h.

- (F01490) Workload gateway-web runs 4 VMs of size 8vCPU/32GB in anti-affinity group AG-1, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01491) Datastore bri-ds27 provides 97 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01492) Cluster ALD-PROD-3 has 31 hosts of model R760 with 96 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01493) Cluster DUN-PREPROD-8 has 7 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01494) Datastore cre-ds55 provides 260 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

## Page 167: Storage policies [compute]

- (F01495) Datastore fer-ds21 provides 289 TB usable on NVMe with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01496) Datastore eas-ds44 provides 162 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01497) Workload identity-queue runs 23 VMs of size 16vCPU/64GB in anti-affinity group AG-20, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01498) Cluster EAS-TEST-5 has 7 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01499) Workload scheduler-app runs 36 VMs of size 16vCPU/64GB in anti-affinity group AG-24, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01500) Workload mailer-queue runs 7 VMs of size 4vCPU/16GB in anti-affinity group AG-11, storage policy bronze and backup tier T2-daily with RPO 24h.

- (F01501) Cluster CRE-PROD-7 has 16 hosts of model DL380g11 with 64 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01502) Workload mailer-app runs 21 VMs of size 4vCPU/16GB in anti-affinity group AG-32, storage policy silver and backup tier T2-daily with RPO 24h.

- (F01503) Cluster DUN-DR-4 has 13 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

## Page 168: Capacity [compute]

- (F01504) Workload reports-app runs 8 VMs of size 4vCPU/16GB in anti-affinity group AG-6, storage policy bronze and backup tier T1-hourly with RPO 1h.

- (F01505) Datastore dun-ds32 provides 67 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01506) Cluster DUN-PREPROD-1 has 8 hosts of model DL380g11 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01507) Workload catalogue-web runs 12 VMs of size 8vCPU/32GB in anti-affinity group AG-22, storage policy gold and backup tier T1-hourly with RPO 24h.

- (F01508) Cluster ALD-MGMT-1 has 30 hosts of model R760 with 64 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01509) Workload telemetry-app runs 20 VMs of size 4vCPU/16GB in anti-affinity group AG-5, storage policy silver and backup tier T3-weekly with RPO 4h.

- (F01510) Cluster FER-MGMT-2 has 19 hosts of model SR650v3 with 64 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01511) Workload mailer-data runs 32 VMs of size 8vCPU/32GB in anti-affinity group AG-23, storage policy bronze and backup tier T2-daily with RPO 4h.

- (F01512) Datastore fer-ds53 provides 225 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 85% used.

## Page 169: Storage policies [compute]

- (F01513) Cluster BRI-DR-3 has 26 hosts of model R760 with 64 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01514) Cluster BRI-PROD-8 has 8 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01515) Datastore cre-ds38 provides 142 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01516) Cluster FER-MGMT-5 has 26 hosts of model R760 with 96 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 3:1.

- (F01517) Cluster DUN-PREPROD-6 has 6 hosts of model R760 with 64 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01518) Workload identity-bastion runs 22 VMs of size 8vCPU/32GB in anti-affinity group AG-9, storage policy silver and backup tier T3-weekly with RPO 24h.

- (F01519) Workload mailer-data runs 2 VMs of size 4vCPU/16GB in anti-affinity group AG-17, storage policy silver and backup tier T1-hourly with RPO 4h.

- (F01520) Workload scheduler-web runs 10 VMs of size 4vCPU/16GB in anti-affinity group AG-33, storage policy bronze and backup tier T2-daily with RPO 4h.

- (F01521) Cluster FER-PREPROD-7 has 5 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

## Page 170: Capacity [compute]

- (F01522) Workload mailer-web runs 8 VMs of size 8vCPU/32GB in anti-affinity group AG-50, storage policy bronze and backup tier T1-hourly with RPO 1h.

- (F01523) Cluster CRE-MGMT-5 has 20 hosts of model DL380g11 with 128 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01524) Cluster DUN-PROD-8 has 27 hosts of model SR650v3 with 128 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01525) Cluster CRE-TEST-1 has 17 hosts of model SR650v3 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01526) Workload gateway-batch runs 39 VMs of size 4vCPU/16GB in anti-affinity group AG-29, storage policy silver and backup tier T2-daily with RPO 24h.

- (F01527) Cluster BRI-MGMT-5 has 16 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01528) Cluster DUN-PREPROD-7 has 4 hosts of model DL380g11 with 64 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01529) Datastore dun-ds02 provides 276 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01530) Datastore ald-ds32 provides 317 TB usable on NVMe with mirror; thin-provisioning ratio 2.0:1 and an alert at 85% used.

## Page 171: Storage policies [compute]

- (F01531) Cluster BRI-DR-9 has 27 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01532) Cluster FER-DR-2 has 14 hosts of model SR650v3 with 64 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01533) Cluster FER-TEST-3 has 25 hosts of model DL380g11 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01534) Workload gateway-data runs 25 VMs of size 4vCPU/16GB in anti-affinity group AG-49, storage policy silver and backup tier T2-daily with RPO 24h.

- (F01535) Datastore eas-ds41 provides 55 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01536) Cluster ALD-TEST-3 has 7 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01537) Workload catalogue-monitoring runs 19 VMs of size 4vCPU/16GB in anti-affinity group AG-23, storage policy gold and backup tier T2-daily with RPO 1h.

- (F01538) Workload gateway-queue runs 3 VMs of size 16vCPU/64GB in anti-affinity group AG-52, storage policy gold and backup tier T1-hourly with RPO 1h.

- (F01539) Cluster CRE-PREPROD-9 has 30 hosts of model SR650v3 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

## Page 172: Storage policies [compute]

- (F01540) Cluster CRE-DR-7 has 7 hosts of model SR650v3 with 96 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 2:1.

- (F01541) Datastore fer-ds31 provides 320 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01542) Cluster FER-DR-9 has 28 hosts of model DL380g11 with 96 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01543) Cluster ALD-PROD-8 has 10 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01544) Workload mailer-bastion runs 2 VMs of size 8vCPU/32GB in anti-affinity group AG-56, storage policy silver and backup tier T1-hourly with RPO 1h.

- (F01545) Cluster EAS-MGMT-9 has 28 hosts of model R760 with 128 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 3:1.

- (F01546) Datastore eas-ds47 provides 194 TB usable on NVMe with mirror; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01547) Workload gateway-queue runs 36 VMs of size 8vCPU/32GB in anti-affinity group AG-19, storage policy gold and backup tier T1-hourly with RPO 1h.

- (F01548) Workload scheduler-queue runs 26 VMs of size 4vCPU/16GB in anti-affinity group AG-18, storage policy silver and backup tier T2-daily with RPO 1h.

## Page 173: Capacity [compute]

- (F01549) Workload catalogue-monitoring runs 21 VMs of size 16vCPU/64GB in anti-affinity group AG-20, storage policy silver and backup tier T1-hourly with RPO 1h.

- (F01550) Workload mailer-data runs 7 VMs of size 4vCPU/16GB in anti-affinity group AG-60, storage policy bronze and backup tier T3-weekly with RPO 24h.

- (F01551) Cluster CRE-PROD-2 has 12 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01552) Cluster EAS-PROD-4 has 5 hosts of model DL380g11 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01553) Datastore eas-ds60 provides 315 TB usable on hybrid with mirror; thin-provisioning ratio 1.5:1 and an alert at 85% used.

- (F01554) Datastore cre-ds07 provides 226 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01555) Datastore cre-ds18 provides 399 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01556) Datastore ald-ds07 provides 264 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01557) Datastore ald-ds17 provides 101 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 75% used.

## Page 174: Storage policies [compute]

- (F01558) Cluster BRI-MGMT-2 has 24 hosts of model R760 with 96 cores and 512 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01559) Cluster BRI-MGMT-4 has 17 hosts of model R760 with 128 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01560) Datastore bri-ds32 provides 300 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01561) Datastore fer-ds25 provides 118 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01562) Workload reports-queue runs 19 VMs of size 4vCPU/16GB in anti-affinity group AG-40, storage policy gold and backup tier T3-weekly with RPO 4h.

- (F01563) Workload identity-web runs 9 VMs of size 8vCPU/32GB in anti-affinity group AG-38, storage policy gold and backup tier T3-weekly with RPO 4h.

- (F01564) Datastore bri-ds37 provides 114 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01565) Cluster BRI-PROD-4 has 11 hosts of model SR650v3 with 64 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01566) Workload scheduler-cache runs 19 VMs of size 4vCPU/16GB in anti-affinity group AG-37, storage policy gold and backup tier T3-weekly with RPO 1h.

## Page 175: Hypervisor clusters [compute]

- (F01567) Datastore ald-ds27 provides 74 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01568) Cluster FER-PROD-6 has 14 hosts of model DL380g11 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01569) Workload identity-cache runs 11 VMs of size 4vCPU/16GB in anti-affinity group AG-25, storage policy silver and backup tier T1-hourly with RPO 24h.

- (F01570) Datastore bri-ds32 provides 270 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01571) Cluster DUN-DR-3 has 5 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01572) Cluster DUN-PROD-5 has 8 hosts of model DL380g11 with 96 cores and 512 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01573) Workload catalogue-monitoring runs 24 VMs of size 8vCPU/32GB in anti-affinity group AG-42, storage policy gold and backup tier T2-daily with RPO 1h.

- (F01574) Datastore cre-ds54 provides 264 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01575) Cluster DUN-PREPROD-1 has 28 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

## Page 176: Capacity [compute]

- (F01576) Datastore fer-ds60 provides 94 TB usable on NVMe with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01577) Datastore cre-ds45 provides 70 TB usable on SAS SSD with mirror; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01578) Datastore dun-ds02 provides 52 TB usable on hybrid with RAID-6; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01579) Workload gateway-data runs 33 VMs of size 16vCPU/64GB in anti-affinity group AG-1, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01580) Datastore eas-ds27 provides 310 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01581) Cluster ALD-TEST-7 has 12 hosts of model SR650v3 with 96 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01582) Workload mailer-app runs 26 VMs of size 8vCPU/32GB in anti-affinity group AG-40, storage policy gold and backup tier T1-hourly with RPO 4h.

- (F01583) Cluster CRE-TEST-8 has 28 hosts of model R760 with 128 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01584) Workload ledger-app runs 8 VMs of size 16vCPU/64GB in anti-affinity group AG-58, storage policy gold and backup tier T1-hourly with RPO 4h.

## Page 177: Hypervisor clusters [compute]

- (F01585) Cluster DUN-DR-9 has 27 hosts of model R760 with 64 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01586) Datastore bri-ds15 provides 397 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

- (F01587) Cluster CRE-PROD-7 has 7 hosts of model DL380g11 with 128 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01588) Cluster CRE-PREPROD-2 has 6 hosts of model DL380g11 with 128 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01589) Cluster ALD-DR-5 has 21 hosts of model R760 with 128 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01590) Workload gateway-bastion runs 23 VMs of size 4vCPU/16GB in anti-affinity group AG-6, storage policy bronze and backup tier T3-weekly with RPO 1h.

- (F01591) Datastore cre-ds01 provides 238 TB usable on hybrid with erasure coding 4+2; thin-provisioning ratio 1.5:1 and an alert at 80% used.

- (F01592) Datastore fer-ds11 provides 33 TB usable on hybrid with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 85% used.

- (F01593) Cluster FER-TEST-4 has 9 hosts of model R760 with 64 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

## Page 178: Workload placement [compute]

- (F01594) Cluster BRI-PREPROD-3 has 13 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01595) Datastore bri-ds03 provides 80 TB usable on hybrid with mirror; thin-provisioning ratio 1.2:1 and an alert at 80% used.

- (F01596) Datastore cre-ds54 provides 371 TB usable on SAS SSD with RAID-6; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01597) Cluster DUN-DR-1 has 9 hosts of model DL380g11 with 64 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01598) Workload catalogue-app runs 12 VMs of size 4vCPU/16GB in anti-affinity group AG-5, storage policy gold and backup tier T2-daily with RPO 1h.

- (F01599) Workload gateway-data runs 19 VMs of size 16vCPU/64GB in anti-affinity group AG-34, storage policy bronze and backup tier T3-weekly with RPO 24h.

- (F01600) Datastore eas-ds58 provides 319 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01601) Datastore fer-ds37 provides 130 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 1.2:1 and an alert at 85% used.

- (F01602) Workload telemetry-batch runs 18 VMs of size 16vCPU/64GB in anti-affinity group AG-14, storage policy bronze and backup tier T1-hourly with RPO 1h.

## Page 179: Backup tiers [compute]

- (F01603) Workload reports-monitoring runs 7 VMs of size 16vCPU/64GB in anti-affinity group AG-8, storage policy bronze and backup tier T1-hourly with RPO 1h.

- (F01604) Cluster FER-MGMT-2 has 21 hosts of model DL380g11 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 4:1.

- (F01605) Datastore bri-ds04 provides 285 TB usable on NVMe with mirror; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01606) Cluster ALD-MGMT-9 has 32 hosts of model R760 with 64 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01607) Workload catalogue-queue runs 18 VMs of size 8vCPU/32GB in anti-affinity group AG-36, storage policy gold and backup tier T1-hourly with RPO 1h.

- (F01608) Workload identity-cache runs 10 VMs of size 4vCPU/16GB in anti-affinity group AG-45, storage policy bronze and backup tier T1-hourly with RPO 24h.

- (F01609) Cluster EAS-DR-2 has 17 hosts of model SR650v3 with 128 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01610) Workload identity-data runs 19 VMs of size 8vCPU/32GB in anti-affinity group AG-2, storage policy gold and backup tier T1-hourly with RPO 1h.

- (F01611) Datastore fer-ds02 provides 390 TB usable on NVMe with RAID-6; thin-provisioning ratio 1.5:1 and an alert at 75% used.

## Page 180: Capacity [compute]

- (F01612) Cluster ALD-PREPROD-8 has 29 hosts of model R760 with 96 cores and 2048 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 3:1.

- (F01613) Cluster FER-MGMT-1 has 27 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 4:1.

- (F01614) Cluster EAS-TEST-5 has 12 hosts of model R760 with 64 cores and 2048 GB RAM each; HA admission control reserves 10% and CPU overcommit is capped at 4:1.

- (F01615) Datastore eas-ds35 provides 264 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 75% used.

- (F01616) Cluster BRI-TEST-9 has 23 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 15% and CPU overcommit is capped at 2:1.

- (F01617) Datastore dun-ds30 provides 33 TB usable on NVMe with mirror; thin-provisioning ratio 1.2:1 and an alert at 75% used.

- (F01618) Datastore cre-ds57 provides 145 TB usable on SAS SSD with erasure coding 4+2; thin-provisioning ratio 2.0:1 and an alert at 80% used.

- (F01619) Cluster CRE-MGMT-5 has 20 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

- (F01620) Cluster DUN-PREPROD-5 has 20 hosts of model R760 with 96 cores and 1024 GB RAM each; HA admission control reserves 25% and CPU overcommit is capped at 2:1.

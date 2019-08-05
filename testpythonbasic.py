#!/usr/bin/python2.7
# coding=utf-8
import sys
from datetime import datetime
from bs4 import BeautifulSoup

currDate = datetime.today().strftime('%Y-%m-%d')
print currDate
print type(currDate)
print type(sys.maxsize)

test01 = "<table id=\"action\"><thead><tr><th><p>序号</p></th><th><p>行动描述</p></th><th><p>预计完成日期</p></th><th><p>状态</p></th><th><p>负责人</p></th></tr></thead><tbody id=\"actionitems\"><tr><td><p><strong>1</strong></p></td><td><p>确定国家队比赛数据供应商</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>2</p></td><td><p>嗨球与创冰完成商务</p></td><td><p>2019年6月5日</p></td><td><p>完成</p></td><td><p>杨龙波</p></td></tr><tr><td><p>3</p></td><td><p>中优Match Tracking Data测试数据（主场：中优）- 改为北体大</p></td><td><p>2019年6月17日</p></td><td><p>进行中</p></td><td><p>李鹏飞</p></td></tr><tr><td><p>4</p></td><td><p>CFA Match Tracking Data上线时间（主场）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>5</p></td><td><p>检查足协预生产系统中国家队比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p>6</p></td><td><p>检查足协预生产系统中国家队竞争对手比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p> 7</p></td><td><p>嗨球主持SAP，嗨球与数据供应商研讨会</p></td><td><p>TBD</p></td><td><p>完成</p></td><td><p>杨龙波/李鹏飞</p></td></tr><tr><td><p>8</p></td><td><p>嗨球与SAP正式数据模拟上线</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>9</p></td><td><p>中优主数据上线时间（嗨球提供数据为6/10）</p></td><td><p>2019年6月18日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>10</p></td><td><p>北体大主数据上线时间（嗨球提供数据为6/17）</p></td><td><p>2019年6月21日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>11</p></td><td><p>CFA主数据上线时间（嗨球提供数据为TBD）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>王宁/Chris</p></td></tr><tr><td><p>12</p></td><td><p>嗨球安排SAP/Amisco/嗨球主数据开发研讨会</p></td><td><p>2019年6月6日</p></td><td><p>进行中</p></td><td><p>王宁</p></td></tr><tr><td><p>13</p></td><td><p>嗨球明确嗨球方负责的数据迁徙所需时间</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/王宁</p></td></tr></tbody></table>"
test02 = "<table id=\"action\"><thead><tr><th><p>序号</p></th><th><p>行动描述</p></th><th><p>预计完成日期</p></th><th><p>状态</p></th><th><p>负责人</p></th></tr></thead><tbody id=\"actionitems\"><tr><td><p><strong>1</strong></p></td><td><p>确定国家队比赛数据供应商</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>2</p></td><td><p>嗨球与创冰完成商务</p></td><td><p>2019年6月5日</p></td><td><p>完成</p></td><td><p>杨龙波</p></td></tr><tr><td><p>3</p></td><td><p>中优Match Tracking Data测试数据（主场：中优）- 改为北体大</p></td><td><p>2019年6月17日</p></td><td><p>进行中</p></td><td><p>李鹏飞</p></td></tr><tr><td><p>4</p></td><td><p>CFA Match Tracking Data上线时间（主场）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>5</p></td><td><p>检查足协预生产系统中国家队比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p>6</p></td><td><p>检查足协预生产系统中国家队竞争对手比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p> 7</p></td><td><p>嗨球主持SAP，嗨球与数据供应商研讨会</p></td><td><p>TBD</p></td><td><p>完成</p></td><td><p>杨龙波/李鹏飞</p></td></tr><tr><td><p>8</p></td><td><p>嗨球与SAP正式数据模拟上线</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>9</p></td><td><p>中优主数据上线时间（嗨球提供数据为6/10）</p></td><td><p>2019年6月18日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>10</p></td><td><p>北体大主数据上线时间（嗨球提供数据为6/17）</p></td><td><p>2019年6月21日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>11</p></td><td><p>CFA主数据上线时间（嗨球提供数据为TBD）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>王宁/Chris</p></td></tr><tr><td><p>12</p></td><td><p>嗨球安排SAP/Amisco/嗨球主数据开发研讨会</p></td><td><p>2019年6月6日</p></td><td><p>进行中</p></td><td><p>王宁</p></td></tr><tr><td><p>13</p></td><td><p>嗨球明确嗨球方负责的数据迁徙所需时间</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/王宁</p></td></tr></tbody></table>"
test04 = "<table id=\"action\"><thead><tr><th><p>序号</p></th><th><p>行动描述</p></th><th><p>预计完成日期</p></th><th><p>状态</p></th><th><p>负责人</p></th></tr></thead><tbody id=\"actionitems\"><tr><td><p><strong>1</strong></p></td><td><p>确定国家队比赛数据供应商</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>2</p></td><td><p>嗨球与创冰完成商务</p></td><td><p>2019年6月5日</p></td><td><p>完成</p></td><td><p>杨龙波</p></td></tr><tr><td><p>3</p></td><td><p>中优Match Tracking Data测试数据（主场：中优）- 改为北体大</p></td><td><p>2019年6月17日</p></td><td><p>进行中</p></td><td><p>李鹏飞</p></td></tr><tr><td><p>4</p></td><td><p>CFA Match Tracking Data上线时间（主场）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>5</p></td><td><p>检查足协预生产系统中国家队比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p>6</p></td><td><p>检查足协预生产系统中国家队竞争对手比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p> 7</p></td><td><p>嗨球主持SAP，嗨球与数据供应商研讨会</p></td><td><p>TBD</p></td><td><p>完成</p></td><td><p>杨龙波/李鹏飞</p></td></tr><tr><td><p>8</p></td><td><p>嗨球与SAP正式数据模拟上线</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>9</p></td><td><p>中优主数据上线时间（嗨球提供数据为6/10）</p></td><td><p>2019年6月18日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>10</p></td><td><p>北体大主数据上线时间（嗨球提供数据为6/17）</p></td><td><p>2019年6月21日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>11</p></td><td><p>CFA主数据上线时间（嗨球提供数据为TBD）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>王宁/Chris</p></td></tr><tr><td><p>12</p></td><td><p>嗨球安排SAP/Amisco/嗨球主数据开发研讨会</p></td><td><p>2019年6月6日</p></td><td><p>进行中</p></td><td><p>王宁</p></td></tr><tr><td><p>13</p></td><td><p>嗨球明确嗨球方负责的数据迁徙所需时间</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/王宁</p></td></tr></tbody></table>"
test05 = "<table id=\"action\"><thead><tr><th><p>序号</p></th><th><p>行动描述</p></th><th><p>预计完成日期</p></th><th><p>状态</p></th><th><p>负责人</p></th></tr></thead><tbody id=\"actionitems\"><tr><td><p><strong>1</strong></p></td><td><p>确定国家队比赛数据供应商</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>2</p></td><td><p>嗨球与创冰完成商务</p></td><td><p>2019年6月5日</p></td><td><p>完成</p></td><td><p>杨龙波</p></td></tr><tr><td><p>3</p></td><td><p>中优Match Tracking Data测试数据（主场：中优）- 改为北体大</p></td><td><p>2019年6月17日</p></td><td><p>进行中</p></td><td><p>李鹏飞</p></td></tr><tr><td><p>4</p></td><td><p>CFA Match Tracking Data上线时间（主场）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>5</p></td><td><p>检查足协预生产系统中国家队比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p>6</p></td><td><p>检查足协预生产系统中国家队竞争对手比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p> 7</p></td><td><p>嗨球主持SAP，嗨球与数据供应商研讨会</p></td><td><p>TBD</p></td><td><p>完成</p></td><td><p>杨龙波/李鹏飞</p></td></tr><tr><td><p>8</p></td><td><p>嗨球与SAP正式数据模拟上线</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>9</p></td><td><p>中优主数据上线时间（嗨球提供数据为6/10）</p></td><td><p>2019年6月18日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>10</p></td><td><p>北体大主数据上线时间（嗨球提供数据为6/17）</p></td><td><p>2019年6月21日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>11</p></td><td><p>CFA主数据上线时间（嗨球提供数据为TBD）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>王宁/Chris</p></td></tr><tr><td><p>12</p></td><td><p>嗨球安排SAP/Amisco/嗨球主数据开发研讨会</p></td><td><p>2019年6月6日</p></td><td><p>进行中</p></td><td><p>王宁</p></td></tr><tr><td><p>13</p></td><td><p>嗨球明确嗨球方负责的数据迁徙所需时间</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/王宁</p></td></tr></tbody></table>"
print test01 == test02
pageValue01 = "<p><a></a>会议情况</p><table><tr><td><p>会议内容: </p></td><td colspan=\"3\"><p>北京体育大学SAP Sports One数据接口会议纪要</p></td></tr><tr><td><p>日期:</p></td><td><p>2019年6月12日</p></td><td><p>时间:</p></td><td><p>14:00-14:30</p></td></tr><tr><td><p>会议地点:</p></td><td><p>Skype Meeting</p></td><td><p>记录人:</p></td><td><p>Chris Deng</p></td></tr><tr><td><p>与会人:</p></td><td colspan=\"3\"><p>嗨球：李鹏飞</p><p>SAP： Chris Deng，Huang He, Wang, Cheng</p></td></tr></table><p>调研情况</p><table><thead><tr><th><p>序号</p></th><th><p>会议情况说明</p></th></tr></thead><tbody><tr><td><p><strong>1</strong></p></td><td><ul><li>更新上次会议的行动计划</li></ul></td></tr><tr><td><p><strong>2</strong></p></td><td><ul><li>SAP与嗨球双方尽量安排同时拜访客户，同时分享会议纪要，确保双方信息一致，信息透明。</li></ul></td></tr><tr><td><p><strong>3</strong></p></td><td><ul><li>如果嗨球有功能需求，请先与SAP顾问团队沟通，以确保功能的完整性和合理性。</li></ul></td></tr><tr><td><p><strong>4</strong></p></td><td><ul><li>内蒙古中优生产系统域名错误，主数据上线时间推迟</li></ul></td></tr><tr><td><p><strong>5</strong></p></td><td><ul><li>黄河主持6/19，6/26日数据会议</li></ul></td></tr></tbody></table><p><a></a>行动计划</p><table id=\"action\"><thead><tr><th><p>序号</p></th><th><p>行动描述</p></th><th><p>预计完成日期</p></th><th><p>状态</p></th><th><p>负责人</p></th></tr></thead><tbody id=\"actionitems\"><tr><td><p><strong>1</strong></p></td><td><p>确定国家队比赛数据供应商</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>2</p></td><td><p>嗨球与创冰完成商务</p></td><td><p>2019年6月5日</p></td><td><p>完成</p></td><td><p>杨龙波</p></td></tr><tr><td><p>3</p></td><td><p>中优Match Tracking Data测试数据（主场：中优）- 改为北体大</p></td><td><p>2019年6月17日</p></td><td><p>进行中</p></td><td><p>李鹏飞</p></td></tr><tr><td><p>4</p></td><td><p>CFA Match Tracking Data上线时间（主场）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>5</p></td><td><p>检查足协预生产系统中国家队比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p>6</p></td><td><p>检查足协预生产系统中国家队竞争对手比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p> 7</p></td><td><p>嗨球主持SAP，嗨球与数据供应商研讨会</p></td><td><p>TBD</p></td><td><p>完成</p></td><td><p>杨龙波/李鹏飞</p></td></tr><tr><td><p>8</p></td><td><p>嗨球与SAP正式数据模拟上线</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>9</p></td><td><p>中优主数据上线时间（嗨球提供数据为6/10）</p></td><td><p>2019年6月18日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>10</p></td><td><p>北体大主数据上线时间（嗨球提供数据为6/17）</p></td><td><p>2019年6月21日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>11</p></td><td><p>CFA主数据上线时间（嗨球提供数据为TBD）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>王宁/Chris</p></td></tr><tr><td><p>12</p></td><td><p>嗨球安排SAP/Amisco/嗨球主数据开发研讨会</p></td><td><p>2019年6月6日</p></td><td><p>进行中</p></td><td><p>王宁</p></td></tr><tr><td><p>13</p></td><td><p>嗨球明确嗨球方负责的数据迁徙所需时间</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/王宁</p></td></tr></tbody></table>"
pageValue02 = "<p><a></a>会议情况</p><table><tr><td><p>会议内容: </p></td><td colspan=\"3\"><p>北京体育大学SAP Sports One数据接口会议纪要</p></td></tr><tr><td><p>日期:</p></td><td><p>2019年6月12日</p></td><td><p>时间:</p></td><td><p>14:00-14:30</p></td></tr><tr><td><p>会议地点:</p></td><td><p>Skype Meeting</p></td><td><p>记录人:</p></td><td><p>Chris Deng</p></td></tr><tr><td><p>与会人:</p></td><td colspan=\"3\"><p>嗨球：李鹏飞</p><p>SAP： Chris Deng，Huang He, Wang, Cheng</p></td></tr></table><p>调研情况</p><table><thead><tr><th><p>序号</p></th><th><p>会议情况说明</p></th></tr></thead><tbody><tr><td><p><strong>1</strong></p></td><td><ul><li>更新上次会议的行动计划</li></ul></td></tr><tr><td><p><strong>2</strong></p></td><td><ul><li>SAP与嗨球双方尽量安排同时拜访客户，同时分享会议纪要，确保双方信息一致，信息透明。</li></ul></td></tr><tr><td><p><strong>3</strong></p></td><td><ul><li>如果嗨球有功能需求，请先与SAP顾问团队沟通，以确保功能的完整性和合理性。</li></ul></td></tr><tr><td><p><strong>4</strong></p></td><td><ul><li>内蒙古中优生产系统域名错误，主数据上线时间推迟</li></ul></td></tr><tr><td><p><strong>5</strong></p></td><td><ul><li>黄河主持6/19，6/26日数据会议</li></ul></td></tr></tbody></table><p><a></a>行动计划</p><table id=\"action\"><thead><tr><th><p>序号</p></th><th><p>行动描述</p></th><th><p>预计完成日期</p></th><th><p>状态</p></th><th><p>负责人</p></th></tr></thead><tbody id=\"actionitems\"><tr><td><p><strong>1</strong></p></td><td><p>确定国家队比赛数据供应商</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>2</p></td><td><p>嗨球与创冰完成商务</p></td><td><p>2019年6月5日</p></td><td><p>完成</p></td><td><p>杨龙波</p></td></tr><tr><td><p>3</p></td><td><p>中优Match Tracking Data测试数据（主场：中优）- 改为北体大</p></td><td><p>2019年6月17日</p></td><td><p>进行中</p></td><td><p>李鹏飞</p></td></tr><tr><td><p>4</p></td><td><p>CFA Match Tracking Data上线时间（主场）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>杨龙波</p></td></tr><tr><td><p>5</p></td><td><p>检查足协预生产系统中国家队比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p>6</p></td><td><p>检查足协预生产系统中国家队竞争对手比赛，导入视频及比赛事件XML</p></td><td><p>2019年5月25日</p></td><td><p>完成</p></td><td><p>王宁</p></td></tr><tr><td><p> 7</p></td><td><p>嗨球主持SAP，嗨球与数据供应商研讨会</p></td><td><p>TBD</p></td><td><p>完成</p></td><td><p>杨龙波/李鹏飞</p></td></tr><tr><td><p>8</p></td><td><p>嗨球与SAP正式数据模拟上线</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>9</p></td><td><p>中优主数据上线时间（嗨球提供数据为6/10）</p></td><td><p>2019年6月18日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>10</p></td><td><p>北体大主数据上线时间（嗨球提供数据为6/17）</p></td><td><p>2019年6月21日</p></td><td><p>进行中</p></td><td><p>李鹏飞/Chris</p></td></tr><tr><td><p>11</p></td><td><p>CFA主数据上线时间（嗨球提供数据为TBD）</p></td><td><p>TBD</p></td><td><p>进行中</p></td><td><p>王宁/Chris</p></td></tr><tr><td><p>12</p></td><td><p>嗨球安排SAP/Amisco/嗨球主数据开发研讨会</p></td><td><p>2019年6月6日</p></td><td><p>进行中</p></td><td><p>王宁</p></td></tr><tr><td><p>13</p></td><td><p>嗨球明确嗨球方负责的数据迁徙所需时间</p></td><td><p>2019年6月12日</p></td><td><p>进行中</p></td><td><p>李鹏飞/王宁</p></td></tr></tbody></table>"
test03 = pageValue01.replace(test01, "")
print test03


htmlfilename = raw_input("Enter the path to the filename -> ")
with open(htmlfilename) as fp:
    soup = BeautifulSoup(fp)

# soup = BeautifulSoup("<html>data</html>")
print soup
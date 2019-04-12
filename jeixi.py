from lxml import etree

text = """
<div class="op_exactqa_itemsArea c-row ">
                
                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E5%80%AA%E5%A4%A7%E7%BA%A2&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="倪大红" target="_blank"><img class="c-img c-img4" src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3085246081,3050308296&amp;fm=58&amp;s=1232798622822FF5C484A8A60300A090"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E5%80%AA%E5%A4%A7%E7%BA%A2&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="倪大红" target="_blank">倪大红</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E9%B9%BF%E6%99%97&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="鹿晗" target="_blank"><img class="c-img c-img4" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1231679303,3089912294&amp;fm=58"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E9%B9%BF%E6%99%97&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="鹿晗" target="_blank">鹿晗</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E5%BC%A0%E8%89%BA%E5%85%B4&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="张艺兴" target="_blank"><img class="c-img c-img4" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1018086398,1698649337&amp;fm=58&amp;s=C6AABB454A73168C2B1D3D260300E040"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E5%BC%A0%E8%89%BA%E5%85%B4&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="张艺兴" target="_blank">张艺兴</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E9%BB%84%E5%AD%90%E9%9F%AC&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="黄子韬" target="_blank"><img class="c-img c-img4" src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3012501073,246089268&amp;fm=58&amp;s=D01B3FD0D0EA6EBF358C09360100E0E0"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E9%BB%84%E5%AD%90%E9%9F%AC&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="黄子韬" target="_blank">黄子韬</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E4%B9%94%E6%8C%AF%E5%AE%87&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="乔振宇" target="_blank"><img class="c-img c-img4" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=4153221186,235546494&amp;fm=58"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E4%B9%94%E6%8C%AF%E5%AE%87&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="乔振宇" target="_blank">乔振宇</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 c-span-last">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E9%83%AD%E4%BA%AC%E9%A3%9E&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="郭京飞" target="_blank"><img class="c-img c-img4" src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=85439245,309577821&amp;fm=58&amp;s=69CA3366CE6392555CEDCC9301008081"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E9%83%AD%E4%BA%AC%E9%A3%9E&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="郭京飞" target="_blank">郭京飞</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E6%98%93%E7%83%8A%E5%8D%83%E7%8E%BA&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="易烊千玺" target="_blank"><img class="c-img c-img4" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=4062622871,4059211183&amp;fm=58"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E6%98%93%E7%83%8A%E5%8D%83%E7%8E%BA&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="易烊千玺" target="_blank">易烊千玺</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E4%BA%8E%E5%B0%8F%E5%BD%A4&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="于小彤" target="_blank"><img class="c-img c-img4" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3487001954,2121633596&amp;fm=58&amp;s=3A8DE7064F5B64CC52C5A9730300607B"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E4%BA%8E%E5%B0%8F%E5%BD%A4&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="于小彤" target="_blank">于小彤</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E9%AB%98%E9%91%AB&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="高鑫" target="_blank"><img class="c-img c-img4" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=3979266063,2850597655&amp;fm=58"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E9%AB%98%E9%91%AB&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="高鑫" target="_blank">高鑫</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E8%83%A1%E6%AD%8C&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="胡歌" target="_blank"><img class="c-img c-img4" src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=4265294863,276161381&amp;fm=58"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E8%83%A1%E6%AD%8C&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="胡歌" target="_blank">胡歌</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 ">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E7%8E%8B%E4%BF%8A%E5%87%AF&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="王俊凯" target="_blank"><img class="c-img c-img4" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=85701420,4125739579&amp;fm=58&amp;s=18A4CF151A3367966E807589030010A0"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E7%8E%8B%E4%BF%8A%E5%87%AF&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="王俊凯" target="_blank">王俊凯</a></p>
                                                        </div>
                                                                                                <div class="op_exactqa_item c-gap-bottom c-span4 c-span-last">
                    <div class="op_exactqa_feedback OP_LOG_BTN">有错误?</div>
                    <p class="op_exactqa_item_img"><a href="/s?rsv_idx=1&amp;wd=%E6%9D%A8%E6%B4%8B&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="杨洋" target="_blank"><img class="c-img c-img4" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=4212266774,1737020032&amp;fm=58&amp;s=67B17C6C5E6BBE5D64E85C060100E0C1"></a></p>
                                        <p class="c-gap-top-small"><a href="/s?rsv_idx=1&amp;wd=%E6%9D%A8%E6%B4%8B&amp;usm=2&amp;nojc=1&amp;ie=utf-8&amp;rsv_cq=%E5%86%85%E5%9C%B0%E7%94%B7%E6%BC%94%E5%91%98&amp;rsv_dl=0_left_exactqa_28266" title="杨洋" target="_blank">杨洋</a></p>
                                                        </div>
                                                                        </div>
"""
html = etree.HTML(text)
# result = etree.tostring(html)
a = html.xpath('//p/a/text()')
print(a)
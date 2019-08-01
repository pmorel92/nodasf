{"filter":false,"title":"models.py","tooltip":"/nodasf/models.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["e"],"id":170},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["x"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["p"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["o"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"remove","lines":["r"],"id":171},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["o"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"remove","lines":["p"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"remove","lines":["x"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"remove","lines":["e"]},{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"remove","lines":["r"]}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":["r"],"id":172}],[{"start":{"row":85,"column":0},"end":{"row":95,"column":0},"action":"remove","lines":["class District(models.Model):","    name = models.CharField(max_length=100, default='')","    description = models.TextField(default=' ')    ","    county = models.ManyToManyField('County')","    cities = models.ManyToManyField('City')","    image = models.ImageField(upload_to='media/stock', default='', blank=True)    ","    slug = models.SlugField(max_length=100, default=' ')    ","  ","    def __str__(self):","        return self.name   ",""],"id":173}],[{"start":{"row":84,"column":8},"end":{"row":85,"column":0},"action":"remove","lines":["",""],"id":174}],[{"start":{"row":98,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["class District(models.Model):","    name = models.CharField(max_length=100, default='')","    description = models.TextField(default=' ')    ","    county = models.ManyToManyField('County')","    cities = models.ManyToManyField('City')","    image = models.ImageField(upload_to='media/stock', default='', blank=True)    ","    slug = models.SlugField(max_length=100, default=' ')    ","  ","    def __str__(self):","        return self.name   ",""],"id":175}],[{"start":{"row":97,"column":28},"end":{"row":98,"column":0},"action":"insert","lines":["",""],"id":176},{"start":{"row":98,"column":0},"end":{"row":98,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":105,"column":0},"end":{"row":106,"column":0},"action":"insert","lines":["",""],"id":177}],[{"start":{"row":105,"column":0},"end":{"row":107,"column":34},"action":"insert","lines":["    city = models.ForeignKey(","        'City',","        on_delete=models.PROTECT,)"],"id":178}],[{"start":{"row":105,"column":7},"end":{"row":105,"column":8},"action":"remove","lines":["y"],"id":179},{"start":{"row":105,"column":6},"end":{"row":105,"column":7},"action":"remove","lines":["t"]},{"start":{"row":105,"column":5},"end":{"row":105,"column":6},"action":"remove","lines":["i"]},{"start":{"row":105,"column":4},"end":{"row":105,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":105,"column":4},"end":{"row":105,"column":5},"action":"insert","lines":["l"],"id":180},{"start":{"row":105,"column":5},"end":{"row":105,"column":6},"action":"insert","lines":["e"]},{"start":{"row":105,"column":6},"end":{"row":105,"column":7},"action":"insert","lines":["v"]},{"start":{"row":105,"column":7},"end":{"row":105,"column":8},"action":"insert","lines":["e"]},{"start":{"row":105,"column":8},"end":{"row":105,"column":9},"action":"insert","lines":["l"]}],[{"start":{"row":106,"column":12},"end":{"row":106,"column":13},"action":"remove","lines":["y"],"id":181},{"start":{"row":106,"column":11},"end":{"row":106,"column":12},"action":"remove","lines":["t"]},{"start":{"row":106,"column":10},"end":{"row":106,"column":11},"action":"remove","lines":["i"]},{"start":{"row":106,"column":9},"end":{"row":106,"column":10},"action":"remove","lines":["C"]}],[{"start":{"row":106,"column":9},"end":{"row":106,"column":10},"action":"insert","lines":["L"],"id":182},{"start":{"row":106,"column":10},"end":{"row":106,"column":11},"action":"insert","lines":["e"]},{"start":{"row":106,"column":11},"end":{"row":106,"column":12},"action":"insert","lines":["v"]},{"start":{"row":106,"column":12},"end":{"row":106,"column":13},"action":"insert","lines":["e"]},{"start":{"row":106,"column":13},"end":{"row":106,"column":14},"action":"insert","lines":["l"]}],[{"start":{"row":106,"column":16},"end":{"row":107,"column":0},"action":"insert","lines":["",""],"id":183},{"start":{"row":107,"column":0},"end":{"row":107,"column":8},"action":"insert","lines":["        "]},{"start":{"row":107,"column":8},"end":{"row":107,"column":9},"action":"insert","lines":["d"]},{"start":{"row":107,"column":9},"end":{"row":107,"column":10},"action":"insert","lines":["e"]},{"start":{"row":107,"column":10},"end":{"row":107,"column":11},"action":"insert","lines":["f"]},{"start":{"row":107,"column":11},"end":{"row":107,"column":12},"action":"insert","lines":["a"]},{"start":{"row":107,"column":12},"end":{"row":107,"column":13},"action":"insert","lines":["u"]},{"start":{"row":107,"column":13},"end":{"row":107,"column":14},"action":"insert","lines":["l"]},{"start":{"row":107,"column":14},"end":{"row":107,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":107,"column":15},"end":{"row":107,"column":16},"action":"insert","lines":["="],"id":184},{"start":{"row":107,"column":16},"end":{"row":107,"column":17},"action":"insert","lines":["1"]},{"start":{"row":107,"column":17},"end":{"row":107,"column":18},"action":"insert","lines":["."]}],[{"start":{"row":107,"column":17},"end":{"row":107,"column":18},"action":"remove","lines":["."],"id":185}],[{"start":{"row":107,"column":17},"end":{"row":107,"column":18},"action":"insert","lines":[","],"id":186},{"start":{"row":107,"column":18},"end":{"row":107,"column":19},"action":"insert","lines":[","]}],[{"start":{"row":107,"column":18},"end":{"row":107,"column":19},"action":"remove","lines":[","],"id":187}],[{"start":{"row":113,"column":0},"end":{"row":114,"column":30},"action":"insert","lines":["    class Meta:","        ordering = ('name',)  "],"id":188}],[{"start":{"row":114,"column":30},"end":{"row":115,"column":0},"action":"insert","lines":["",""],"id":189},{"start":{"row":115,"column":0},"end":{"row":115,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":151,"column":36},"end":{"row":152,"column":0},"action":"insert","lines":["",""],"id":190},{"start":{"row":152,"column":0},"end":{"row":152,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":152,"column":0},"end":{"row":155,"column":34},"action":"insert","lines":["    level = models.ForeignKey(","        'Level',","        default=1,","        on_delete=models.PROTECT,)"],"id":191}],[{"start":{"row":153,"column":13},"end":{"row":153,"column":14},"action":"remove","lines":["l"],"id":192},{"start":{"row":153,"column":12},"end":{"row":153,"column":13},"action":"remove","lines":["e"]},{"start":{"row":153,"column":11},"end":{"row":153,"column":12},"action":"remove","lines":["v"]},{"start":{"row":153,"column":10},"end":{"row":153,"column":11},"action":"remove","lines":["e"]},{"start":{"row":153,"column":9},"end":{"row":153,"column":10},"action":"remove","lines":["L"]}],[{"start":{"row":153,"column":9},"end":{"row":153,"column":10},"action":"insert","lines":["V"],"id":193},{"start":{"row":153,"column":10},"end":{"row":153,"column":11},"action":"insert","lines":["e"]},{"start":{"row":153,"column":11},"end":{"row":153,"column":12},"action":"insert","lines":["n"]},{"start":{"row":153,"column":12},"end":{"row":153,"column":13},"action":"insert","lines":["u"]},{"start":{"row":153,"column":13},"end":{"row":153,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":152,"column":8},"end":{"row":152,"column":9},"action":"remove","lines":["l"],"id":194},{"start":{"row":152,"column":7},"end":{"row":152,"column":8},"action":"remove","lines":["e"]},{"start":{"row":152,"column":6},"end":{"row":152,"column":7},"action":"remove","lines":["v"]},{"start":{"row":152,"column":5},"end":{"row":152,"column":6},"action":"remove","lines":["e"]},{"start":{"row":152,"column":4},"end":{"row":152,"column":5},"action":"remove","lines":["l"]}],[{"start":{"row":152,"column":4},"end":{"row":152,"column":5},"action":"insert","lines":["V"],"id":195},{"start":{"row":152,"column":5},"end":{"row":152,"column":6},"action":"insert","lines":["e"]},{"start":{"row":152,"column":6},"end":{"row":152,"column":7},"action":"insert","lines":["n"]},{"start":{"row":152,"column":7},"end":{"row":152,"column":8},"action":"insert","lines":["u"]},{"start":{"row":152,"column":8},"end":{"row":152,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":152,"column":4},"end":{"row":152,"column":5},"action":"remove","lines":["V"],"id":196}],[{"start":{"row":152,"column":4},"end":{"row":152,"column":5},"action":"insert","lines":["v"],"id":197}],[{"start":{"row":118,"column":47},"end":{"row":118,"column":51},"action":"remove","lines":["    "],"id":198},{"start":{"row":118,"column":47},"end":{"row":119,"column":0},"action":"insert","lines":["",""]},{"start":{"row":119,"column":0},"end":{"row":119,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":119,"column":0},"end":{"row":119,"column":60},"action":"insert","lines":["    homepage = models.CharField(max_length=300, default=' ')"],"id":199}],[{"start":{"row":125,"column":19},"end":{"row":126,"column":0},"action":"insert","lines":["",""],"id":200},{"start":{"row":126,"column":0},"end":{"row":126,"column":8},"action":"insert","lines":["        "]},{"start":{"row":126,"column":8},"end":{"row":126,"column":9},"action":"insert","lines":["n"]},{"start":{"row":126,"column":9},"end":{"row":126,"column":10},"action":"insert","lines":["u"]},{"start":{"row":126,"column":10},"end":{"row":126,"column":11},"action":"insert","lines":["l"]},{"start":{"row":126,"column":11},"end":{"row":126,"column":12},"action":"insert","lines":["l"]},{"start":{"row":126,"column":12},"end":{"row":126,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":126,"column":13},"end":{"row":126,"column":14},"action":"insert","lines":["T"],"id":201},{"start":{"row":126,"column":14},"end":{"row":126,"column":15},"action":"insert","lines":["r"]},{"start":{"row":126,"column":15},"end":{"row":126,"column":16},"action":"insert","lines":["u"]},{"start":{"row":126,"column":16},"end":{"row":126,"column":17},"action":"insert","lines":["e"]},{"start":{"row":126,"column":17},"end":{"row":126,"column":18},"action":"insert","lines":[","]}],[{"start":{"row":145,"column":19},"end":{"row":145,"column":23},"action":"remove","lines":["    "],"id":202},{"start":{"row":145,"column":19},"end":{"row":146,"column":0},"action":"insert","lines":["",""]},{"start":{"row":146,"column":0},"end":{"row":146,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":146,"column":0},"end":{"row":146,"column":18},"action":"insert","lines":["        null=True,"],"id":203}],[{"start":{"row":245,"column":7},"end":{"row":246,"column":0},"action":"insert","lines":["",""],"id":204},{"start":{"row":246,"column":0},"end":{"row":246,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":245,"column":7},"end":{"row":245,"column":17},"action":"insert","lines":["null=True,"],"id":205}],[{"start":{"row":241,"column":19},"end":{"row":241,"column":23},"action":"remove","lines":["    "],"id":206},{"start":{"row":241,"column":19},"end":{"row":242,"column":0},"action":"insert","lines":["",""]},{"start":{"row":242,"column":0},"end":{"row":242,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":242,"column":8},"end":{"row":242,"column":18},"action":"insert","lines":["null=True,"],"id":207}],[{"start":{"row":321,"column":0},"end":{"row":322,"column":0},"action":"insert","lines":["",""],"id":208},{"start":{"row":322,"column":0},"end":{"row":323,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":321,"column":0},"end":{"row":322,"column":41},"action":"insert","lines":["    class Meta:","        ordering = ('-date_updated',)    "],"id":209}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":28},"action":"remove","lines":["        return self.name    "],"id":213},{"start":{"row":18,"column":0},"end":{"row":18,"column":50},"action":"insert","lines":["        return \"{}/{}\".format(self.id, self.story)"]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":25},"action":"remove","lines":["        return self.name "],"id":214},{"start":{"row":11,"column":0},"end":{"row":11,"column":50},"action":"insert","lines":["        return \"{}/{}\".format(self.id, self.story)"]}],[{"start":{"row":57,"column":0},"end":{"row":57,"column":28},"action":"remove","lines":["        return self.name    "],"id":215},{"start":{"row":57,"column":0},"end":{"row":57,"column":50},"action":"insert","lines":["        return \"{}/{}\".format(self.id, self.story)"]}],[{"start":{"row":66,"column":0},"end":{"row":66,"column":50},"action":"insert","lines":["        return \"{}/{}\".format(self.id, self.story)"],"id":216}],[{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "],"id":217},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["r"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["e"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["t"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["u"]}],[{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["r"],"id":218},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["n"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":[" "]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["s"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["e"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["l"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["f"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["."]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["n"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["a"]},{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["m"]}],[{"start":{"row":66,"column":50},"end":{"row":66,"column":51},"action":"remove","lines":["e"],"id":219}],[{"start":{"row":18,"column":44},"end":{"row":18,"column":49},"action":"remove","lines":["story"],"id":220},{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"insert","lines":["n"]},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["a"]},{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"insert","lines":["m"]},{"start":{"row":18,"column":47},"end":{"row":18,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":11,"column":44},"end":{"row":11,"column":49},"action":"remove","lines":["story"],"id":221},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"insert","lines":["n"]},{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"insert","lines":["a"]},{"start":{"row":11,"column":46},"end":{"row":11,"column":47},"action":"insert","lines":["m"]},{"start":{"row":11,"column":47},"end":{"row":11,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":57,"column":44},"end":{"row":57,"column":49},"action":"remove","lines":["story"],"id":222},{"start":{"row":57,"column":44},"end":{"row":57,"column":45},"action":"insert","lines":["n"]},{"start":{"row":57,"column":45},"end":{"row":57,"column":46},"action":"insert","lines":["a"]},{"start":{"row":57,"column":46},"end":{"row":57,"column":47},"action":"insert","lines":["m"]},{"start":{"row":57,"column":47},"end":{"row":57,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":66,"column":44},"end":{"row":66,"column":49},"action":"remove","lines":["story"],"id":223},{"start":{"row":66,"column":44},"end":{"row":66,"column":45},"action":"insert","lines":["n"]},{"start":{"row":66,"column":45},"end":{"row":66,"column":46},"action":"insert","lines":["a"]},{"start":{"row":66,"column":46},"end":{"row":66,"column":47},"action":"insert","lines":["m"]},{"start":{"row":66,"column":47},"end":{"row":66,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":75,"column":34},"end":{"row":75,"column":38},"action":"remove","lines":["    "],"id":224},{"start":{"row":75,"column":34},"end":{"row":76,"column":0},"action":"insert","lines":["",""]},{"start":{"row":76,"column":0},"end":{"row":76,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":76,"column":4},"end":{"row":76,"column":5},"action":"insert","lines":["d"],"id":225},{"start":{"row":76,"column":5},"end":{"row":76,"column":6},"action":"insert","lines":["e"]},{"start":{"row":76,"column":6},"end":{"row":76,"column":7},"action":"insert","lines":["s"]},{"start":{"row":76,"column":7},"end":{"row":76,"column":8},"action":"insert","lines":["c"]},{"start":{"row":76,"column":8},"end":{"row":76,"column":9},"action":"insert","lines":["r"]},{"start":{"row":76,"column":9},"end":{"row":76,"column":10},"action":"insert","lines":["i"]},{"start":{"row":76,"column":10},"end":{"row":76,"column":11},"action":"insert","lines":["p"]},{"start":{"row":76,"column":11},"end":{"row":76,"column":12},"action":"insert","lines":["t"]},{"start":{"row":76,"column":12},"end":{"row":76,"column":13},"action":"insert","lines":["i"]},{"start":{"row":76,"column":13},"end":{"row":76,"column":14},"action":"insert","lines":["o"]},{"start":{"row":76,"column":14},"end":{"row":76,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":76,"column":15},"end":{"row":76,"column":16},"action":"insert","lines":[":"],"id":226}],[{"start":{"row":76,"column":16},"end":{"row":76,"column":17},"action":"insert","lines":[" "],"id":227}],[{"start":{"row":76,"column":16},"end":{"row":76,"column":17},"action":"remove","lines":[" "],"id":228},{"start":{"row":76,"column":15},"end":{"row":76,"column":16},"action":"remove","lines":[":"]}],[{"start":{"row":76,"column":15},"end":{"row":76,"column":16},"action":"insert","lines":[" "],"id":229},{"start":{"row":76,"column":16},"end":{"row":76,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":76,"column":17},"end":{"row":76,"column":18},"action":"insert","lines":[" "],"id":230},{"start":{"row":76,"column":18},"end":{"row":76,"column":19},"action":"insert","lines":["T"]},{"start":{"row":76,"column":19},"end":{"row":76,"column":20},"action":"insert","lines":["e"]},{"start":{"row":76,"column":20},"end":{"row":76,"column":21},"action":"insert","lines":["x"]}],[{"start":{"row":76,"column":18},"end":{"row":76,"column":21},"action":"remove","lines":["Tex"],"id":231},{"start":{"row":76,"column":18},"end":{"row":76,"column":27},"action":"insert","lines":["TextField"]}],[{"start":{"row":76,"column":27},"end":{"row":76,"column":29},"action":"insert","lines":["()"],"id":232}],[{"start":{"row":76,"column":28},"end":{"row":76,"column":29},"action":"insert","lines":["d"],"id":233},{"start":{"row":76,"column":29},"end":{"row":76,"column":30},"action":"insert","lines":["e"]},{"start":{"row":76,"column":30},"end":{"row":76,"column":31},"action":"insert","lines":["f"]},{"start":{"row":76,"column":31},"end":{"row":76,"column":32},"action":"insert","lines":["a"]},{"start":{"row":76,"column":32},"end":{"row":76,"column":33},"action":"insert","lines":["u"]},{"start":{"row":76,"column":33},"end":{"row":76,"column":34},"action":"insert","lines":["l"]},{"start":{"row":76,"column":34},"end":{"row":76,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":76,"column":35},"end":{"row":76,"column":36},"action":"insert","lines":["="],"id":234}],[{"start":{"row":76,"column":36},"end":{"row":76,"column":37},"action":"insert","lines":[" "],"id":235}],[{"start":{"row":76,"column":36},"end":{"row":76,"column":37},"action":"remove","lines":[" "],"id":236}],[{"start":{"row":76,"column":36},"end":{"row":76,"column":38},"action":"insert","lines":["''"],"id":237}],[{"start":{"row":76,"column":37},"end":{"row":76,"column":38},"action":"insert","lines":[" "],"id":238}],[{"start":{"row":76,"column":18},"end":{"row":76,"column":19},"action":"insert","lines":["m"],"id":239},{"start":{"row":76,"column":19},"end":{"row":76,"column":20},"action":"insert","lines":["o"]},{"start":{"row":76,"column":20},"end":{"row":76,"column":21},"action":"insert","lines":["d"]},{"start":{"row":76,"column":21},"end":{"row":76,"column":22},"action":"insert","lines":["e"]},{"start":{"row":76,"column":22},"end":{"row":76,"column":23},"action":"insert","lines":["l"]},{"start":{"row":76,"column":23},"end":{"row":76,"column":24},"action":"insert","lines":["s"]},{"start":{"row":76,"column":24},"end":{"row":76,"column":25},"action":"insert","lines":["."]}],[{"start":{"row":7,"column":79},"end":{"row":7,"column":82},"action":"remove","lines":["   "],"id":240},{"start":{"row":7,"column":79},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":49},"action":"insert","lines":["    description = models.TextField(default=' ')  "],"id":241}],[{"start":{"row":104,"column":9},"end":{"row":104,"column":10},"action":"remove","lines":["y"],"id":242}],[{"start":{"row":104,"column":9},"end":{"row":104,"column":10},"action":"insert","lines":["i"],"id":243},{"start":{"row":104,"column":10},"end":{"row":104,"column":11},"action":"insert","lines":["e"]},{"start":{"row":104,"column":11},"end":{"row":104,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":244}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":31},"action":"insert","lines":["def get_image_url(self):","        return 'Image url here'"],"id":245}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":246}],[{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":247},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["l"],"id":248},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["r"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["u"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["_"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"remove","lines":["e"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"remove","lines":["g"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"remove","lines":["a"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"remove","lines":["m"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["i"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["d"],"id":249},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["i"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["s"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["t"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["r"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["i"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["c"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":16},"end":{"row":14,"column":30},"action":"remove","lines":["Image url here"],"id":250},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["n"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["a"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["m"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":86,"column":25},"end":{"row":87,"column":0},"action":"insert","lines":["",""],"id":251},{"start":{"row":87,"column":0},"end":{"row":87,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":87,"column":0},"end":{"row":88,"column":21},"action":"insert","lines":["    def get_district(self):","        return 'name'"],"id":252}],[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["e"],"id":253},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["m"]}],[{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["'"],"id":254},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"remove","lines":["a"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["n"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"remove","lines":["'"]}],[{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["s"],"id":255},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["e"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["l"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["f"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["."]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["n"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["a"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["m"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":88,"column":20},"end":{"row":88,"column":21},"action":"remove","lines":["'"],"id":256},{"start":{"row":88,"column":19},"end":{"row":88,"column":20},"action":"remove","lines":["e"]},{"start":{"row":88,"column":18},"end":{"row":88,"column":19},"action":"remove","lines":["m"]},{"start":{"row":88,"column":17},"end":{"row":88,"column":18},"action":"remove","lines":["a"]},{"start":{"row":88,"column":16},"end":{"row":88,"column":17},"action":"remove","lines":["n"]},{"start":{"row":88,"column":15},"end":{"row":88,"column":16},"action":"remove","lines":["'"]}],[{"start":{"row":88,"column":15},"end":{"row":88,"column":16},"action":"insert","lines":["s"],"id":257},{"start":{"row":88,"column":16},"end":{"row":88,"column":17},"action":"insert","lines":["e"]},{"start":{"row":88,"column":17},"end":{"row":88,"column":18},"action":"insert","lines":["l"]},{"start":{"row":88,"column":18},"end":{"row":88,"column":19},"action":"insert","lines":["f"]},{"start":{"row":88,"column":19},"end":{"row":88,"column":20},"action":"insert","lines":["."]},{"start":{"row":88,"column":20},"end":{"row":88,"column":21},"action":"insert","lines":["n"]},{"start":{"row":88,"column":21},"end":{"row":88,"column":22},"action":"insert","lines":["a"]},{"start":{"row":88,"column":22},"end":{"row":88,"column":23},"action":"insert","lines":["m"]},{"start":{"row":88,"column":23},"end":{"row":88,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":186,"column":19},"end":{"row":186,"column":23},"action":"remove","lines":["    "],"id":258},{"start":{"row":186,"column":19},"end":{"row":187,"column":0},"action":"insert","lines":["",""]},{"start":{"row":187,"column":0},"end":{"row":187,"column":8},"action":"insert","lines":["        "]},{"start":{"row":187,"column":8},"end":{"row":187,"column":9},"action":"insert","lines":["n"]},{"start":{"row":187,"column":9},"end":{"row":187,"column":10},"action":"insert","lines":["u"]},{"start":{"row":187,"column":10},"end":{"row":187,"column":11},"action":"insert","lines":["l"]},{"start":{"row":187,"column":11},"end":{"row":187,"column":12},"action":"insert","lines":["l"]},{"start":{"row":187,"column":12},"end":{"row":187,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":187,"column":13},"end":{"row":187,"column":14},"action":"insert","lines":["T"],"id":259},{"start":{"row":187,"column":14},"end":{"row":187,"column":15},"action":"insert","lines":["r"]},{"start":{"row":187,"column":15},"end":{"row":187,"column":16},"action":"insert","lines":["u"]},{"start":{"row":187,"column":16},"end":{"row":187,"column":17},"action":"insert","lines":["e"]},{"start":{"row":187,"column":17},"end":{"row":187,"column":18},"action":"insert","lines":[","]}],[{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"remove","lines":["d"],"id":260},{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"remove","lines":["i"]}],[{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"insert","lines":["n"],"id":261},{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"insert","lines":["a"]},{"start":{"row":12,"column":37},"end":{"row":12,"column":38},"action":"insert","lines":["m"]},{"start":{"row":12,"column":38},"end":{"row":12,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":46},"end":{"row":12,"column":50},"action":"remove","lines":["name"],"id":262},{"start":{"row":12,"column":46},"end":{"row":12,"column":47},"action":"insert","lines":["i"]},{"start":{"row":12,"column":47},"end":{"row":12,"column":48},"action":"insert","lines":["d"]}],[{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"remove","lines":["d"],"id":263},{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"remove","lines":["i"]}],[{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":["n"],"id":264},{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"insert","lines":["a"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["m"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":22,"column":46},"end":{"row":22,"column":50},"action":"remove","lines":["name"],"id":265},{"start":{"row":22,"column":46},"end":{"row":22,"column":47},"action":"insert","lines":["i"]},{"start":{"row":22,"column":47},"end":{"row":22,"column":48},"action":"insert","lines":["d"]}],[{"start":{"row":61,"column":47},"end":{"row":61,"column":48},"action":"remove","lines":["e"],"id":266},{"start":{"row":61,"column":46},"end":{"row":61,"column":47},"action":"remove","lines":["m"]},{"start":{"row":61,"column":45},"end":{"row":61,"column":46},"action":"remove","lines":["a"]},{"start":{"row":61,"column":44},"end":{"row":61,"column":45},"action":"remove","lines":["n"]}],[{"start":{"row":61,"column":44},"end":{"row":61,"column":45},"action":"insert","lines":["i"],"id":267},{"start":{"row":61,"column":45},"end":{"row":61,"column":46},"action":"insert","lines":["d"]},{"start":{"row":61,"column":46},"end":{"row":61,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":61,"column":46},"end":{"row":61,"column":47},"action":"remove","lines":["e"],"id":268}],[{"start":{"row":61,"column":36},"end":{"row":61,"column":37},"action":"remove","lines":["d"],"id":269},{"start":{"row":61,"column":35},"end":{"row":61,"column":36},"action":"remove","lines":["i"]}],[{"start":{"row":61,"column":35},"end":{"row":61,"column":36},"action":"insert","lines":["n"],"id":270},{"start":{"row":61,"column":36},"end":{"row":61,"column":37},"action":"insert","lines":["a"]},{"start":{"row":61,"column":37},"end":{"row":61,"column":38},"action":"insert","lines":["m"]},{"start":{"row":61,"column":38},"end":{"row":61,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":70,"column":36},"end":{"row":70,"column":37},"action":"remove","lines":["d"],"id":271},{"start":{"row":70,"column":35},"end":{"row":70,"column":36},"action":"remove","lines":["i"]}],[{"start":{"row":70,"column":35},"end":{"row":70,"column":36},"action":"insert","lines":["n"],"id":272},{"start":{"row":70,"column":36},"end":{"row":70,"column":37},"action":"insert","lines":["a"]},{"start":{"row":70,"column":37},"end":{"row":70,"column":38},"action":"insert","lines":["m"]},{"start":{"row":70,"column":38},"end":{"row":70,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":70,"column":46},"end":{"row":70,"column":50},"action":"remove","lines":["name"],"id":273},{"start":{"row":70,"column":46},"end":{"row":70,"column":47},"action":"insert","lines":["i"]},{"start":{"row":70,"column":47},"end":{"row":70,"column":48},"action":"insert","lines":["d"]}]]},"ace":{"folds":[],"scrolltop":1618,"scrollleft":0,"selection":{"start":{"row":63,"column":6},"end":{"row":63,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"state":"start","mode":"ace/mode/python"}},"timestamp":1564525659224,"hash":"212e2cc679131da69861f7d4590785cf0e8b5011"}
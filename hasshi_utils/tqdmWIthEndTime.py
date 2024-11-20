from tqdm.auto import tqdm
from datetime import datetime, timedelta
from collections import OrderedDict
import time

# tqdm インスタンスを作成する際にカスタムフォーマットを設定するヘルパー関数
def tqdmWithEndtime(iterable, *args, **kwargs):
    kwargs['bar_format'] = kwargs.get('bar_format', '{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]{postfix}')
    pbar = tqdm(iterable, *args, **kwargs)
    
    # 開始時刻を設定
    postfix = OrderedDict()
    start_time = datetime.now()
    postfix["start"] = start_time.strftime('%H:%M')
    for item in iterable:
        # 現在時刻と終了予定時刻を計算
        current_time = datetime.now()
        elapsed = (current_time - start_time).total_seconds()
        if pbar.n + 1 < pbar.total:  # 終了予定時刻の計算
            estimated_end_time = start_time + timedelta(seconds=elapsed / (pbar.n + 1) * (pbar.total - (pbar.n + 1)))
        else:
            estimated_end_time = current_time
        
        # カスタム情報の追加（postfixで表示）

        postfix["curr"] = current_time.strftime('%H:%M')
        postfix["end"] = estimated_end_time.strftime('%H:%M')
        
        
        pbar.set_postfix(
            postfix
        )
        
        yield item  # イテレートして次の要素を返す
        pbar.update(1)  # 進捗を更新

    pbar.close()  # 最後にプログレスバーを閉じる
# tf_mem_growth_hook
silly way to set gpu_options.allow_growth True by default in TensorFlow

TensorFlow 파이썬 라이브러리의 gpu_options.allow_growth 기본값을 True로 만들어줍니다.

Python import 함수를 감싸서, "tensorflow" 이름의 모듈을 import할 때 import가 모두 끝난 뒤 다음 Class의 생성자에 gpu_options.allow_growth 값을 True로 설정하는 코드를 덧붙입니다.

''Session, InteractiveSession, ConfigProto''

## 사용법
* 본 저장소를 clone합니다.
* ''$ bash ./install.sh'' 하면
  * "~/path/to/site-packages/" 경로에 imphook_tf.py를 복사하고, sitecustomize.py 파일을 만들거나 덧붙여 파이썬 실행 시 앞의 스크립트가 수행되도록 합니다.
* 끝!
 
### 삭제하려면
* "~/path/to/site-packages/" 경로에 가서
* ''imphook_tf.py'' 파일을 삭제하고
* ''sitecustomize.py'' 파일을 열어서 ''imphook_tf'' 모듈을 실행하는 부분을 삭제하거나, ''sitecustomize.py'' 파일을 다른 용도로 사용하지 않는다면 그냥 삭제하세요.

## 왜 필요한가?

TensorFlow 세션이 시작되면, 기본적으로 메모리 파편화를 피하고 성능 최대화를 위해 GPU 메모리 전체를 세션이 차지하도록 되어 있는 것으로 알고 있습니다.

이로 인해 여러 사용자가 한 GPU를 동시에 사용하는 일이 어렵게 됩니다.

이를 피하기 위해, 세션 옵션으로 gpu_options.allow_growth를 주면 성능 저하를 대가로 GPU 메모리 전체 대신 필요한 만큼만 할당받게 됩니다.

이러한 옵션을 매번 코드에 짜넣는 일이 귀찮기 때문에, 이 옵션을 기본값으로 줄 수 있도록 하는 스크립트를 만들었습니다.

파이썬 실행시 <~/path/to/site-packages/sitecustomize.py> 파일을 읽어들여 사용자 레벨 초기화를 수행하는데, 여기에서 위 hook 모듈을 실행합니다.

물론, GPU 하나로 한 사람이 쓰기에도 벅찬 게 사실이라 사실 별 의미는 없습니다. 언젠가는 TensorFlow 기본 기능으로 더 예쁘게 구현될 수 있기도 하겠고요.

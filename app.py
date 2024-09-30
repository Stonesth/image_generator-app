import replicate

input = {
    "width": 856,
    "height": 1156,
    "prompt": "a white-haired young woman wearing a flower crown, a very large fiery dragon, castle in the background, illustration in the style of WHMSCPE001",
    "output_format": "png",
    "output_quality": 100,
    "num_inference_steps": 25
}

output = replicate.run(
    "bingbangboom-lab/flux-new-whimscape:2e8de10f217bc56da163a0204cf09f89995eaf643459014803fae79753183682",
    input=input
)
print(output)
#=> ["https://replicate.delivery/yhqm/tiRsqyv36EZLJJkZWTv8VC9...